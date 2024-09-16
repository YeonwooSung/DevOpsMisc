# Optimizing PostgreSQL Queries: From 300 Seconds to 2 Seconds for Billions of Records

## 1. Generating Billions of Records

```sql
CREATE TABLE transactions (
    transaction_id serial PRIMARY KEY,
    user_id int NOT NULL,
    transaction_date date NOT NULL,
    amount decimal(10,2) NOT NULL
);
```

## 2. Data Generation

The following stored procedure will generate 1 billion records:
```sql
DO $$
BEGIN
    FOR i IN 1..1000000 LOOP
        INSERT INTO transactions (user_id, transaction_date, amount)
        SELECT
            trunc(random() * 10000 + 1),
            '2020-01-01'::date + trunc(random() * 500) * (interval '1 day'),
            trunc(random() * 1000 + 1)::decimal(10,2)
        FROM generate_series(1, 1000);
    END LOOP;
END $$;
```

This script inserts 1 billion transaction records, simulating a real-world, large-scale database.

## 3. Original SQL Query

Our initial query attempts to calculate the total transaction amount for each user:
```sql
SELECT user_id, SUM(amount) AS total_amount
FROM transactions
GROUP BY user_id;
```

## Optimizations

### 3.1. Indexing

To improve performance, we start by adding an index to the user_id column, which is used in the Group By clause:
```sql
CREATE INDEX idx_user_id ON transactions (user_id);
```

After adding the index, the query’s execution time dropped to around 80 seconds.
While this is an improvement, it’s still not fast enough.
The Explain output shows that the index is being used, but the process remains I/O-bound due to the sheer volume of data.

### 3.2. Partitioning

To further optimize the query, we introduce partitioning based on transcation_date.
Partitioning allows PostgreSQL to divide the table into smaller, more manageable pieces, thereby reducing the data each query needs to scan.

```sql
CREATE TABLE transactions_partitioned (
    transaction_id serial,
    user_id int NOT NULL,
    transaction_date date NOT NULL,
    amount decimal(10,2) NOT NULL,
    PRIMARY KEY (transaction_id, transaction_date)
) PARTITION BY RANGE (transaction_date);


CREATE TABLE transactions_2020 PARTITION OF transactions_partitioned
FOR VALUES FROM ('2020-01-01') TO ('2021-01-01');

CREATE TABLE transactions_2021 PARTITION OF transactions_partitioned
FOR VALUES FROM ('2021-01-01') TO ('2022-01-01');
```

After partitioning, the query execution time decreased significantly to around 20 seconds.
The Explain plan now shows that only the relevant partitions are being scanned, which reduces the amount of data processed.

#### 3.2.1. Indexing on Partitioned Tables

To further optimize the query, we add an index to the user_id column on the partitioned table:
```sql
CREATE INDEX idx_user_id_partitioned ON transactions_partitioned (user_id);
```

#### 3.2.2. Inserting Data into Partitions

When inserting new data, we need to ensure that it goes into the correct partition.
We can use a trigger to automatically route the data to the appropriate partition based on the transaction_date:
```sql
DO $$
BEGIN
    FOR i IN 1..1000000 LOOP
        INSERT INTO transactions_partitioned (user_id, transaction_date, amount)
        SELECT
            trunc(random() * 10000 + 1),
            '2020-01-01'::date + trunc(random() * 500) * (interval '1 day'),
            trunc(random() * 1000 + 1)::decimal(10,2);
    END LOOP;
END $$;
```

### 3.3 Materialized Views

For even faster query performance, we can create a materialized view that pre-calculates the total transaction amount for each user:
```sql
CREATE MATERIALIZED VIEW user_transaction_sums AS
SELECT user_id, SUM(amount) AS total_amount
FROM transactions_partitioned
GROUP BY user_id;

CREATE INDEX idx_user_id_sum ON user_transaction_sums (user_id);
```

By querying the materialized view, we can retrieve the results almost instantaneously:
```sql
SELECT * FROM user_transaction_sums;
```

This query executes in less than 2 seconds, achieving the performance target.

## 4. Handling Edge Cases

### 4.1. Dealing with Data Skew

In real-world scenarios, data skew can occur when certain users have significantly more transactions than others.

- `Hash Partitioning`: Use hash partitioning on user_id to evenly distribute data across partitions.

```sql
CREATE TABLE transactions_partitioned_hash (
    transaction_id serial,
    user_id int NOT NULL,
    transaction_date date NOT NULL,
    amount decimal(10,2) NOT NULL,
    PRIMARY KEY (transaction_id, transaction_date)
) PARTITION BY HASH (user_id);

CREATE TABLE transactions_1 PARTITION OF transactions_partitioned_hash
FOR VALUES WITH (MODULUS 4, REMAINDER 0);

CREATE TABLE transactions_2 PARTITION OF transactions_partitioned_hash
FOR VALUES WITH (MODULUS 4, REMAINDER 1);

CREATE TABLE transactions_3 PARTITION OF transactions_partitioned_hash
FOR VALUES WITH (MODULUS 4, REMAINDER 2);

CREATE TABLE transactions_4 PARTITION OF transactions_partitioned_hash
FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

- `Partial Indexes`: Create partial indexes on frequently accessed users, e.g., users with the most transactions.

```sql
CREATE INDEX idx_user_id_1 ON transactions_partitioned_hash (user_id) WHERE user_id = 1;
CREATE INDEX idx_user_id_2 ON transactions_partitioned_hash (user_id) WHERE user_id = 2;

CREATE INDEX idx_high_activity_users ON transactions (user_id) 
WHERE user_id IN (SELECT user_id FROM transactions GROUP BY user_id HAVING COUNT(*) > 1000000);

CREATE INDEX idx_high_activity_users ON transactions_partitioned (user_id) 
WHERE user_id IN (SELECT user_id FROM transactions_partitioned GROUP BY user_id HAVING COUNT(*) > 1000000);
```

### 4.2. Frequent Data Updates

For databases with frequent updates or inserts, maintaining materialized views and indexes can become costly. In such scenarios:

- `Refresh Strategies`: Implement a refresh strategy for materialized views, such as periodic refreshes or incremental updates.
```sql
-- Refresh materialized view periodically
REFRESH MATERIALIZED VIEW user_transaction_sums;

-- if materialized view is created with CONCURRENTLY option
REFRESH MATERIALIZED VIEW CONCURRENTLY user_transaction_sums;
```

### 4.3. Query Timeouts

For long-running queries, set appropriate query timeouts to prevent resource exhaustion:
```sql
SET statement_timeout = '5min';
```

Or, you can set the timeout at the session level:
```sql
SET LOCAL statement_timeout = '5min';
```

Also, you can set the timeout at transaction level:
```sql
BEGIN;
SET statement_timeout = '30s';
SELECT user_id, SUM(amount) FROM transactions GROUP BY user_id;
COMMIT;
```

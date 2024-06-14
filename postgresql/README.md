# PostgreSQL

PostgreSQL is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance.

PostgreSQL features transactions with Atomicity, Consistency, Isolation, Durability (ACID) properties, automatically updatable views, materialized views, triggers, foreign keys, and stored procedures.

It is designed to handle a range of workloads, from single machines to data warehouses or Web services with many concurrent users.
It was the default database for macOS Server and is also available for Linux, FreeBSD, OpenBSD, and Windows.

## Queries for monitoring (DevOps)

- [Run vacuum manually with verbose output](./monitoring/manual_verbose_vacuum.sql)
- [Turn off autovacuum for a particular table](./monitoring/alter_table_turn_autovacuum_off.sql)
- [Retrieve information about blocked and blocking processes in the database](./monitoring/retrieve_blocked_processes.sql)
- [Retrieve dead tuples](./monitoring//retrieve_dead_tuples.sql)
- [Get session information about currently running VACUUM](./monitoring/get_vacuum_info.sql)
- [Get Top 20 oldest tables](./monitoring/get_20_oldest_tables.sql)
- [Stop long query by terminating long query session](./monitoring/terminate_long_query_session.sql)

## Postgres based Interesting Projects

**[CloudNative-PG](https://github.com/cloudnative-pg/cloudnative-pg)**:
CloudNativePG is a Kubernetes operator that covers the full lifecycle of a PostgreSQL database cluster with a primary/standby architecture, using native streaming replication

## Aurora PostgreSQL supported extensions

**[Extension versions for Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Extensions.html)**

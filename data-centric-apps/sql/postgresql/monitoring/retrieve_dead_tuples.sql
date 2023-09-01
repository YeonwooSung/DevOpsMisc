
-- 일반적으로 Auto Vacuum 대상은 "dead tuple"이 20% 이상인 경우로 선정된다.
-- 즉, dead tuple의 비율이 20% 이상인 테이블을 찾는 방법을 알아야 한다.

-- The SELECT statement specifies the columns to be returned in the result set.
-- relname AS TableName retrieves the name of the table.
-- n_live_tup AS LiveTuples retrieves the number of live tuples (rows) in the table.
-- n_dead_tup AS DeadTuples retrieves the number of dead tuples (rows) in the table.
-- n_dead_tup / n_live_tup AS ratio calculates the ratio of dead tuples to live tuples.
-- last_autovacuum AS Autovacuum retrieves the timestamp of the last autovacuum operation on the table.
-- last_autoanalyze AS Autoanalyze retrieves the timestamp of the last autoanalyze operation on the table.
-- * retrieves all columns from the pg_stat_user_tables view.
-- The FROM clause specifies the source table or view, which is pg_stat_user_tables in this case.
-- The WHERE clause filters the result set based on the condition n_dead_tup > 0, which selects only tables with at least one dead tuple.

SELECT
relname AS TableName,
n_live_tup AS LiveTuples,
n_dead_tup AS DeadTuples,
n_dead_tup / n_live_tup AS ratio,
last_autovacuum AS Autovacuum,
last_autoanalyze AS Autoanalyze,
*
FROM pg_stat_user_tables
WHERE n_dead_tup > 0;

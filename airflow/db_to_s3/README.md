# DB to S3

Simple example for using Airflow to extract data from DB, and upload to S3 bucket.

## Files

- [extract_mongodb.py](./extract_mongodb.py) : Extract documents from mongodb, and upload to the S3
- [extract_mysql_full.py](./extract_mysql_full.py) : Extract full data from MySQL DB
- [extract_mysql_incremental.py](./extract_mysql_incremental.py) : Extract data from MySQL DB with incremental extract pattern
- [mysql_bin_log.py](./mysql_bin_log.py) : Extract binary logs from MySQL DB by using mysql-replication, and upload binlog to the S3
- [pipeline.conf](./pipeline.conf) : configuration file
- [sample_mongodb.py](./sample_mongodb.py) : Python script to insert mock data into mongodb for testing
- [sample.sql](./sample.sql) : Simple SQL script for generating table and inserting mock data

## Dependency

This example uses airflow 2.5.1, thus, it might not be compatible with the airflow that is pre-installed in your machine.
So, please make sure use virtual-env with suitable python library versions.

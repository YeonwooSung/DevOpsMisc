# SQL Scripts

This directory contains example SQL scripts for various databases.

## Table of Contents

## Simple Order Service

Defining SQL scripts for a simple order service.

- Create Tables
    - [Create Order table and Customer table](./order_service/create_order_and_customer_tables.sql)
    - [Create Product table and ProductAttribute table](./order_service/create_product_tables.sql)
- Create Indexes
    - IBM DB2
        * [Create Indexes for Customer table](./order_service/create_customer_index.db2.sql)
        * [Create Indexes for Product table](./order_service/create_product_index.db2.sql)
    - Microsoft Access
        * [Create Indexes for Customer table](./order_service/create_customer_index.access.sql)
    - SQL Server
        * [Create Indexes for Customer table](./order_service/create_customer_index.sqlserver.sql)
    - Oracle
        * [Create Indexes for Customer table](./order_service/create_customer_index.oracle.sql)
    - PostgreSQL
        * [Create Indexes for Customer table](./order_service/create_customer_index.postgresql.sql)
- Create Triggers
    - SQL Server
        * [Create Triggers for Order table](./order_service/trigger_for_order_update.sql_server.sql)
- Create Views
    - [Create Views for normalizing the denormalized table](./order_service/create_views.sql)

-- Create index to products table
-- This file contains example command for IBM DB2
-- In DB2, you need to explicitly define the "EXCLUDE NULL KEYS" option to exclude null values from the index
CREATE UNIQUE INDEX ProductID_IDX
    ON Products (ProductNumber ASC)
    EXCLUDE NULL KEYS;

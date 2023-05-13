-- Create index on Customer table
-- This file contains command for IBM DB2.
-- In DB2, you need to explicitly define the "EXCLUDE NULL KEYS" option to exclude null values from the index
CREATE INDEX CustPhone_IDX
    ON Customer (CustPhoneNumber)
    EXCLUDE NULL KEYS;

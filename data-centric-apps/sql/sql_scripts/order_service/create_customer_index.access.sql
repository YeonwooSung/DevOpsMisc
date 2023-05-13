-- Create index on Customer table
-- This file contains sample command for Microsoft Access.
-- In Access, you need to explicitly define the "WITH IGNORE NULL" option to exclude null values from the index
-- This is because the Access database allows NULL value to be stored in the index
-- It is also possible to prevent NULL values by using "WITH DISALLOW NULL" option
CREATE INDEX CustPhone_IDX
    ON Customer (CustPhoneNumber)
    WITH IGNORE NULL;

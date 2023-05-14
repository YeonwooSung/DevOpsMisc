-- Create index on Customer table
-- This file contains sample command for Oracle DB.
-- In Oracle DB, we could use 'NVL' function to convert NULL to default value
-- In this case, we convert NULL to 'unknown'
CREATE INDEX CustPhone_IDX ON Customer (NVL(CustPhoneNumber, 'unknown'));

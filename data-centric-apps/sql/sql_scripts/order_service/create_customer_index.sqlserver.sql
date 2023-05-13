-- Create index on Customer table
-- This file contains command for SQL Server.
CREATE INDEX CustPhone_IDX
    ON Customer (CustPhoneNumber)
    WHERE CustPhoneNumber IS NOT NULL;

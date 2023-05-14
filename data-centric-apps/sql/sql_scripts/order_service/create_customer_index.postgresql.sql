-- Create index on Customer table
-- This file contains sample command for PostgreSQL.

-- Use WHERE clause to filter out NULL values
CREATE INDEX CustPhone_IDX ON Customer (CustPhoneNumber) WHERE CustPhoneNumber IS NOT NULL;

-- Use 'COALESCE' function to convert NULL to default value
CREATE INDEX CustPhone_IDX ON Customer (COALESCE(CustPhoneNumber, 'unknown'));

-- Use 'CASE' function to convert NULL to default value
CREATE INDEX CustPhone_IDX ON Customer (CASE WHEN CustPhoneNumber IS NULL THEN 'unknown' ELSE CustPhoneNumber END);

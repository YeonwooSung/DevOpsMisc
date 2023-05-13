-- Create Customer table
CREATE TABLE IF NOT EXISTS Customer (
    CustomerID int NOT NULL PRIMARY KEY,
    CustFirstName varchar(25) NULL,
    CustLastName varchar(25) NULL,
    CustStreetAddress varchar(50) NULL,
    CustCity varchar(30) NULL,
    CustState varchar(2) NULL,
    CustZipCode varchar(10) NULL,
    CustAreaCode smallint NULL DEFAULT 0,
    CustPhoneNumber varchar(8) NULL
);

-- Create Order table
CREATE TABLE IF NOT EXISTS Orders (
    OrderNumber int NOT NULL PRIMARY KEY,
    OrderDate date NULL,
    ShipDate date NULL,
    CustomerID int NOT NULL DEFAULT 0,
    EmployeeID int NOT NULL DEFAULT 0,
    OrderTotal decimal(15, 2) NULL DEFAULT 0
);

-- Define foreign key relationship
ALTER TABLE Orders ADD CONSTRAINT FK_Orders_Customer FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID);
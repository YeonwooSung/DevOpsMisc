-- Create Products Table
CREATE TABLE IF NOT EXISTS products (
    ProductNumber int NOT NULL PRIMARY KEY,
    ProductName varchar(255) NOT NULL,
    ProductDescription varchar(255) NOT NULL,
);

-- Create ProductAttributes Table
CREATE TABLE IF NOT EXISTS ProductAttributes (
    ProductNumber int NOT NULL,
    AttributeName varchar(255) NOT NULL,
    AttributeValue varchar(255) NOT NULL,
    PRIMARY KEY (ProductNumber, AttributeName)
);

-- Define Foreign Key Constraint
ALTER TABLE ProductAttributes
    ADD CONSTRAINT fk_ProductAttributes_Products
    FOREIGN KEY (ProductNumber) REFERENCES Products(ProductNumber);

CREATE TABLE Items (
    ItemID INT PRIMARY KEY,
    ItemName VARCHAR(255),
    ItemPrice DECIMAL(10, 2)
);

CREATE TABLE Stock (
    ItemID INT,
    Quantity INT,
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    ItemID INT,
    PaymentAmount DECIMAL(10, 2),
    PaymentDate DATE,
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

CREATE TABLE Refunds (
    RefundID INT PRIMARY KEY,
    PaymentID INT,
    RefundAmount DECIMAL(10, 2),
    RefundDate DATE,
    FOREIGN KEY (PaymentID) REFERENCES Payments(PaymentID)
);

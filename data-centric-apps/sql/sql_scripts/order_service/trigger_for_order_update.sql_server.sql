-- A Trigger for Order Update
CREATE TRIGGER updateOrdersOrderTotals
    ON Orders
    AFTER INSERT, DELETE, UPDATE
AS
BEGIN UPDATE Orders
    SET OrderTotal = (
        SELECT SUM(QuantityOrdered * QuotedPrice)
        FROM Order_Details OD
        WHERE OD.OrderNumber = Orders.OrderNumber
    )
    WHERE Orders.OrderNumber IN (
        SELECT OrderNumber FROM inserted
        UNION
        SELECT OrderNumber FROM deleted
    );
END;
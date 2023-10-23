-- Users table stores user information.

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(100),
    Email VARCHAR(100),
    Password VARCHAR(100)
);

-- SubscriptionPlans table stores information about the different subscription plans.

CREATE TABLE SubscriptionPlans (
    PlanID INT PRIMARY KEY,
    PlanName VARCHAR(50),
    PlanDescription VARCHAR(255)
);


-- UserSubscriptions table stores information about which user is subscribed to which plan. It has foreign keys to both the Users and SubscriptionPlans tables.

CREATE TABLE UserSubscriptions (
    UserID INT,
    PlanID INT,
    SubscriptionDate DATE,
    PRIMARY KEY (UserID, PlanID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (PlanID) REFERENCES SubscriptionPlans(PlanID)
);

-- Items table stores information about the items (movies, series, etc.).
-- Each item is associated with a plan, and only users subscribed to that plan (or a higher plan) can access the item. It has a foreign key to the SubscriptionPlans table.

CREATE TABLE Items (
    ItemID INT PRIMARY KEY,
    ItemName VARCHAR(100),
    ItemDescription VARCHAR(255),
    PlanID INT,
    FOREIGN KEY (PlanID) REFERENCES SubscriptionPlans(PlanID)
);

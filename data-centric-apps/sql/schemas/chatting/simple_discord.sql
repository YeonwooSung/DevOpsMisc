-- Each user has a unique ID, username, and email.
-- Each server has a unique ID, a name, and an owner (which is a user).
-- Each channel has a unique ID, a name, and belongs to a server.
-- Each message has a unique ID, content, belongs to a user (the author of the message), is posted in a channel, and has a timestamp indicating when it was posted.

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Servers (
    ServerID INT PRIMARY KEY,
    ServerName VARCHAR(255) NOT NULL,
    OwnerID INT,
    FOREIGN KEY (OwnerID) REFERENCES Users(UserID)
);

CREATE TABLE Channels (
    ChannelID INT PRIMARY KEY,
    ChannelName VARCHAR(255) NOT NULL,
    ServerID INT,
    FOREIGN KEY (ServerID) REFERENCES Servers(ServerID)
);

CREATE TABLE Messages (
    MessageID INT PRIMARY KEY,
    Content TEXT NOT NULL,
    UserID INT,
    ChannelID INT,
    TimeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ChannelID) REFERENCES Channels(ChannelID)
);

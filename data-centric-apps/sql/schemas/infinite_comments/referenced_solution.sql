CREATE TABLE comments (
    id INT PRIMARY KEY,
    parent_id INT,
    text VARCHAR(255),
    created_at TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES comments(id)
);

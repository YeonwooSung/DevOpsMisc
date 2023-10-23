-- 경로 열거 기반

CREATE TABLE comment (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    path VARCHAR(255) NOT NULL,
    level INT NOT NULL
);

INSERT INTO comment (id, name, path, level)
VALUES (1, 'comment 1', '1', 0);

INSERT INTO comment (id, name, path, level)
VALUES (2, 'comment 2', '2', 0);

INSERT INTO comment (id, name, path, level)
VALUES (3, 'comment 3', '3', 0);

INSERT INTO comment (id, name, path, level)
VALUES (4, 'comment 1-1', '1-1', 1);

INSERT INTO comment (id, name, path, level)
VALUES (5, 'comment 1-2', '1-2', 1);

INSERT INTO comment (id, name, path, level)
VALUES (6, 'comment 1-1-1', '1-1-1', 2);

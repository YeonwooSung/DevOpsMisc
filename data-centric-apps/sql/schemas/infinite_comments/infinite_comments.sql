CREATE TABLE comments (
    id INT PRIMARY KEY,
    content VARCHAR(255),
    created_at TIMESTAMP,
    del BOOLEAN,
    ref INT,
    re_step INT,
    re_level INT,
);

-- REF는 댓글끼리 묶는 기능, re_step으로 순서를 나타내고, re_level은 들여쓰기를 나타낸다

INSERT INTO comments (id, content, created_at, del, ref, re_step, re_level)
VALUES (1, 'comment 1', '2019-01-01 00:00:00', false, 1, 0, 0);

INSERT INTO comments (id, content, created_at, del, ref, re_step, re_level)
VALUES (2, 'comment 2', '2019-01-01 00:01:00', false, 2, 0, 0);

INSERT INTO comments (id, content, created_at, del, ref, re_step, re_level)
VALUES (3, 'comment 3', '2019-01-01 00:02:00', false, 3, 0, 0);

INSERT INTO comments (id, content, created_at, del, ref, re_step, re_level)
VALUES (4, 'comment 1-1', '2019-01-01 00:03:01', false, 1, 1, 1);

INSERT INTO comments (id, content, created_at, del, ref, re_step, re_level)
VALUES (5, 'comment 1-2', '2019-01-01 00:04:01', false, 1, 2, 1);

INSERT INTO comments (id, content, created_at, del, ref, re_step, re_level)
VALUES (6, 'comment 1-1-1', '2019-01-01 00:04:06', false, 1, 2, 1);

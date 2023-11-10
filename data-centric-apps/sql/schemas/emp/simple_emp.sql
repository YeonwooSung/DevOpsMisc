--
-- 계층화된 조직도를 SQL로 구현하기
--

-- 테이블 생성
CREATE TABLE employee (
    id BIGINT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    manager_id BIGINT REFERENCES employee(id)
)


-- Select Employee and their manager
SELECT e.id, e.first_name, e.role, e.manager_id, m.first_name
FROM employee e
LEFT JOIN employee m ON e.manager_id = m.id;

-- Select Part of Organization Tree
WITH empdata AS (
    (SELECT id, first_name, role, manager_id, 1 AS level
    FROM employee
    WHERE id = 4)
    UNION ALL
    (SELECT this.id, this.first_name, this.role, this.manager_id, prior.level + 1
    FROM empdata prior
    INNER JOIN employee this ON this.manager_id = prior.id)
)
SELECT e.id, e.first_name, e.role, e.manager_id, e.level
FROM empdata e
ORDER BY e.level;

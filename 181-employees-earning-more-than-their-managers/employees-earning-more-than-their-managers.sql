# Write your MySQL query statement below
SELECT e.name as Employee
FROM Employee AS e
INNER JOIN Employee AS e2
    ON e.managerid = e2.id
WHERE e.salary > e2.salary;
-- CTE ---------------------------------------------------
-- CTE (Common Table Expression) is a temporary result set that you can define within a query to simplify complex SQL statements.

-- Use case-1: We want to calculate the average salary per department and then find all employees whose salary is above the average salary of their department.

WITH avg_sal AS(
    SELECT dept, AVG(salary) AS avg_salary FROM employee GROUP BY dept
)

SELECT 
    e.emp_id,e.fname,e.dept,e.salary,a.avg_salary
FROM employee e 
JOIN avg_sal a ON e.dept=a.dept 
WHERE e.salary > a.avg_salary;


-- Use case-2: We want to find the highest-paid employee in each department.

WITH max_sal AS(
    SELECT dept, MAX(salary) AS max_salary FROM employee GROUP BY dept
)

SELECT 
    e.emp_id,e.fname,e.dept,e.salary,m.max_salary
FROM employee e 
JOIN max_sal m ON e.dept=m.dept 
WHERE e.salary = m.max_salary;

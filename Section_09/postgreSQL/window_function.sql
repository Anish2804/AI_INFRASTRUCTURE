-- WINDOW FUNCTION -----
-- Window functions, also known as analytic functions allow you to perform calculations across a set of rows related to the current row. 
-- Defined by an OVER() clause.

-- Running sum query
SELECT fname,salary,
    SUM(salary) OVER(ORDER BY salary)
    FROM employee;

-- Running avg query
SELECT fname,salary,
    AVG(salary) OVER(ORDER BY salary)
    FROM employee;

-- ROW_NUMBER
SELECT 
    ROW_NUMBER() OVER(),
    fname,salary
    FROM employee;

SELECT 
    ROW_NUMBER() OVER(PARTITION BY dept),
    fname,dept,salary
    FROM employee;


-- RANK
SELECT 
    fname,salary,
    RANK() OVER(ORDER BY salary DESC)
    FROM employee;


-- DENSE_RANK
SELECT 
    fname,salary,
    DENSE_RANK() OVER(ORDER BY salary DESC)
    FROM employee;


-- LAG
SELECT 
    fname,salary,
    LAG(salary) OVER()
    FROM employee;


-- LEAD
SELECT 
    fname,salary,
    LEAD(salary) OVER(ORDER BY salary DESC)
    FROM employee;

SELECT 
    fname,salary,
    (salary-LEAD(salary) OVER(ORDER BY salary DESC)) as salary_diff
    FROM employee;













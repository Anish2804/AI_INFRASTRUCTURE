SELECT COUNT(emp_id) From employee;

SELECT SUM(salary) FROM employee;

SELECT AVG(salary) FROM employee;

SELECT MIN(salary) FROM employee;

SELECT MAX(salary) FROM employee;


-- GROUP BY

SELECT dept FROM employee GROUP BY dept;

SELECT dept,COUNT(emp_id) FROM employee GROUP BY dept;

SELECT dept,COUNT(emp_id),SUM(salary) FROM employee GROUP BY dept;
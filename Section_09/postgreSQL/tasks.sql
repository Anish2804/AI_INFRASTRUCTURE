SELECT concat_ws(':',emp_id,fname,lname,dept) from employee WHEre emp_id=1;

SELECT concat_ws(':',emp_id,concat_ws(' ',fname,lname),dept,salary) from employee WHEre emp_id=1;

SELECT concat_ws(':',emp_id,fname,UPPER(dept)) from employee WHERE emp_id=4;

SELECT concat(LEFT(dept,1),emp_id), fname FROM  employee;

SELECT COUNT(*) AS total_employees FROM employee;

SELECT dept, COUNT(*) AS total_employees FROM employee GROUP BY dept;

SELECT MIN(salary) AS lowest_salary FROM employee;

SELECT MAX(salary) AS highest_salary FROM employee;

SELECT SUM(salary) AS total_salary FROM employee WHERE dept = 'Loan';

SELECT dept, AVG(salary) AS average_salary FROM employee GROUP BY dept;

SELECT DISTINCT dept FROM employee;

SELECT * FROM employee ORDER BY salary DESC;

SELECT * FROM employee ORDER BY salary DESC LIMIT 3;

SELECT * FROM employee WHERE fname LIKE 'A%';

SELECT * FROM employee WHERE LENGTH(fname) = 4;



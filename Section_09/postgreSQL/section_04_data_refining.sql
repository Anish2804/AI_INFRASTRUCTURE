SELECT * FROM employee;

SELECT * FROM employee WHERE dept='HR';


SELECT * FROM employee WHERE salary >= 50000;


SELECT * FROM employee WHERE salary >= 50000 or dept='HR';


SELECT * FROM employee WHERE salary >= 50000 and dept='IT';


SELECT * FROM employee WHERE dept IN ('HR','IT','FINANCE');


SELECT * FROM employee WHERE dept NOT IN ('HR','IT','Finance');


SELECT * From employee WHERE salary BETWEEN 50000 AND 60000;


SELECT DISTINCT dept FROM employee;


SELECT * FROM employee ORDER BY fname;


SELECT * FROM employee ORDER BY emp_id DESC;


SELECT * FROM employee LIMIT 3;


SELECT * FROM employee WHERE fname LIKE 'A%';


SELECT * FROM employee WHERE fname LIKE '%a';


SELECT * FROM employee WHERE fname LIKE '%i%';


SELECT * FROM employee WHERE dept LIKE '__';


SELECT * FROM employee WHERE fname LIKE '_a%';


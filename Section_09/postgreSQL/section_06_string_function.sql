-- concat
SELECT concat(fname,lname) FROM employee;
SELECT emp_id,concat(fname,lname) AS Fullname,dept FROM employee;

-- concat_ws
SELECT concat_ws('-',fname,lname) FROM employee;
SELECT emp_id,concat_ws('-',fname,lname) AS Fullname,dept FROM employee;

-- SUBSTRING
SELECT substr('HELLO ANISH',1,5);
SELECT substr('HELLO ANISH',7,12);

-- REPLACE
SELECT replace('HEY ANISH','HEY','HELLO');
SELECT REPLACE(dept,'IT','TECH') from employee;

--REVERSE
SELECT reverse(fname) FROM employee;

-- LENGTH
SELECT * FROM employee WHERE LENGTH(fname) > 4;

-- UPPER/LOWER
SELECT upper(fname) FROM employee;
SELECT lower(fname) FROM employee;

-- LEFT/RIGHT/TRIM/POSITION
SELECT LEFT('hello world',4);
SELECT RIGHT('hello world',5);
SELECT LENGTH (TRIM('    Alright     '));
SELECT position('om' in 'Thomas');


  
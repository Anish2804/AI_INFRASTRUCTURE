-- Add table
ALTER TABLE person
ADD COLUMN age INT DEFAULT  0;

-- Remove table
ALTER TABLE person
DROP COLUMN age ;

-- Rename column name
ALTER TABLE person
RENAME COLUMN name TO full_name;

--Rename table name
ALTER TABLE insaan
RENAME TO person;

ALTER TABLE person
ALTER COLUMN fUll_name
SET DATA TYPE VARCHAR(200); 

ALTER TABLE person
ALTER COLUMN fUll_name
SET DEFAULT 'unknown'; 

ALTER TABLE person
ALTER COLUMN fUll_name
SET NOT NULL; 


-- CHECK CONSTRAINS
ALTER TABLE person
ADD COLUMN mob VARCHAR(15) CHECK (LENGTH(mob)>=10);

INSERT INTO person(mob)
VALUES (1234567890);

ALTER TABLE person
DROP CONSTRAINT person_mob_check;

ALTER TABLE person
ADD CONSTRAINT person_mob_check CHECK (mob!=NULL);


-- NAMED CONSTRAINT
ALTER TABLE person
ADD CONSTRAINT mob_no_less_than_10 CHECK (LENGTH(mob)>=10);

INSERT INTO person(mob)
VALUES (12345690);

INSERT INTO person(mob)
VALUES (1234567890);



-- EXPRESSION CASE

-- CASE
SELECT fname,salary,
CASE 
    WHEN salary>=50000 THEN  'High'
    ELSE 'Low'
END AS sal_cat
FROM employee; 
    

SELECT fname,salary,
CASE 
    WHEN salary>=55000 THEN  'High'
    WHEN salary BETWEEN 48000 AND 55000
        THEN 'Mid'
    ELSE 'Low'
END AS sal_cat
FROM employee; 


-- task 1
SELECT fname, salary, ROUND(salary * 0.10) AS bonus
FROM employee;
    
-- task 2
SELECT 
CASE 
    WHEN salary>=55000 THEN  'High'
    WHEN salary BETWEEN 48000 AND 55000
        THEN 'Mid'
    ELSE 'Low'
END AS sal_cat,COUNT(emp_id)
FROM employee
GROUP BY sal_cat;




SELECT * FROM person;
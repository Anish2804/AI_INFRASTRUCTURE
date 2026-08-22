-- Creating the table
CREATE TABLE person(
    id int,
    name VARCHAR(100),
    city VARCHAR(100)
);


-- Inserting the table
INSERT INTO person(id,name,city)
VALUES 
(101,'aaaaa','bhopal'),
(102,'bbbbb','dhanbad'),
(103,'ccccc','gurgoan'),
(104,'ddddd','bangalore');


-- Reading the table
SELECT * FROM person;


-- Updating the table
UPDATE person 
    SET city='patna'
WHERE id=101;


-- Updating the table
DELETE FROM person
WHERE id=104;




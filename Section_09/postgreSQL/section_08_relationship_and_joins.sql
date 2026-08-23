CREATE TABLE customers (
    cust_id SERIAL PRIMARY KEY,
    cust_name VARCHAR(100) NOT NULL
);

CREATE TABLE orders (
    ord_id SERIAL PRIMARY KEY,
    ord_date DATE NOT NULL,
    price NUMERIC NOT NULL,
    cust_id INTEGER NOT NULL,
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);

INSERT INTO customers (cust_name)
VALUES
    ('Raju'),
    ('Sham'),
    ('Paul'),
    ('Alex');


INSERT INTO orders (ord_date, cust_id, price)
VALUES
    ('2024-01-01', 1, 250.00),
    ('2024-01-15', 1, 300.00),
    ('2024-02-01', 2, 150.00),
    ('2024-03-01', 3, 450.00),
    ('2024-04-04', 2, 550.00);


SELECT * FROM customers;

SELECT * FROM orders;


TRUNCATE TABLE orders, customers RESTART IDENTITY CASCADE;   --table ke andar ka saara data remove karta hai aur IDs ko reset karta hai





-- ONE-TO-MANY EXAMPLES ----------------------------


-- CROSS JOIN
SELECT * FROM customers CROSS JOIN orders;

-- INNER JOIN
SELECT * FROM customers c 
INNER JOIN 
orders O
ON c.cust_id = O.cust_id;

SELECT c.cust_name,COUNT(O.ord_id) FROM customers c 
INNER JOIN 
orders O
ON c.cust_id = O.cust_id
GROUP BY cust_name;

SELECT c.cust_name,SUM(O.price) FROM customers c 
INNER JOIN 
orders O
ON c.cust_id = O.cust_id
GROUP BY cust_name;


-- LEFT JOIN
SELECT * FROM customers c 
LEFT JOIN 
orders O
ON c.cust_id = O.cust_id;

-- RIGHT JOIN
SELECT * FROM customers c 
RIGHT JOIN 
orders O
ON c.cust_id = O.cust_id;





-- MANY-TO-MANY ----------------------------- WOKING ON INSTITUTE DB

CREATE TABLE students (
    s_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE courses (
    c_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    fee NUMERIC NOT NULL
);

CREATE TABLE enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    s_id INT NOT NULL,
    c_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (s_id) REFERENCES students(s_id),
    FOREIGN KEY (c_id) REFERENCES courses(c_id)
);


INSERT INTO Students (name) VALUES
('Raju'),
('Sham'),
('Alex');

INSERT INTO courses (name, fee)
VALUES
('Mathematics', 500.00),
('Physics', 600.00),
('Chemistry', 700.00);

INSERT INTO enrollment (s_id, c_id, enrollment_date)
VALUES
(1, 1, '2024-01-01'), -- Raju enrolled in Mathematics
(1, 2, '2024-01-15'), -- Raju enrolled in Physics
(2, 1, '2024-02-01'), -- Sham enrolled in Mathematics
(2, 3, '2024-02-15'), -- Sham enrolled in Chemistry
(3, 3, '2024-03-25'); -- Alex enrolled in Chemistry

SELECT * FROM students;

SELECT * FROM courses;

SELECT * FROM enrollment;


SELECT s.name, c.name, e.enrollment_date, c.fee FROM
enrollment e 
JOIN students s ON e.s_id=s.s_id
JOIN courses c ON e.c_id=c.c_id;








-- PRACTICE EXERCISE WOKING ON STORE DB -----------------------------------------------

CREATE TABLE customers (
    cust_id SERIAL PRIMARY KEY,
    cust_name VARCHAR(100) NOT NULL
);

CREATE TABLE orders (
    ord_id SERIAL PRIMARY KEY,
    ord_date DATE NOT NULL,
    cust_id INTEGER NOT NULL,
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);

CREATE TABLE products (
    p_id SERIAL PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL,
    price NUMERIC NOT NULL
);

CREATE TABLE order_items (
    item_id SERIAL PRIMARY KEY,
    ord_id INTEGER NOT NULL,
    p_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (ord_id) REFERENCES orders(ord_id),
    FOREIGN KEY (p_id) REFERENCES products(p_id)
);


INSERT INTO customers (cust_name)
VALUES
    ('Raju'), ('Sham'), ('Paul'), ('Alex');

INSERT INTO orders (ord_date, cust_id)
VALUES
    ('2024-01-01', 1),  -- Raju first order
    ('2024-02-01', 2),  -- Sham first order
    ('2024-03-01', 3),  -- Paul first order
    ('2024-04-04', 2);  -- Sham second order

INSERT INTO products (p_name, price)
VALUES
    ('Laptop', 55000.00),
    ('Mouse', 500),
    ('Keyboard', 800.00),
    ('Cable', 250.00)
;

INSERT INTO order_items (ord_id, p_id, quantity)
VALUES
    (1, 1, 1),  -- Raju ordered 1 Laptop
    (1, 4, 2),  -- Raju ordered 2 Cables
    (2, 1, 1),  -- Sham ordered 1 Laptop
    (3, 2, 1),  -- Paul ordered 1 Mouse
    (3, 4, 5),  -- Paul ordered 5 Cables
    (4, 3, 1);  -- Sham ordered 1 Keyboard


SELECT c.cust_name,o.ord_date,p.p_name,p.price,oi.quantity,(oi.quantity*p.price) AS total_price
FROM order_items oi 
JOIN products p ON oi.p_id=p.p_id
JOIN orders o ON o.ord_id=oi.ord_id
JOIN customers c ON c.cust_id=o.cust_id


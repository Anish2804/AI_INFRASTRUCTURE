-- UNDERSTADING VIEWS--->        ek virtual table jo kisi SELECT query ke result ko represent karta hai.
--                               Data actually duplicate/store nahi hota; query save hoti hai.

CREATE VIEW billing_info AS 
SELECT 
    c.cust_name,
    o.ord_date,
    p.p_name,
    p.price,
    oi.quantity,
    (oi.quantity*p.price) AS total_price
FROM order_items oi 
    JOIN products p ON oi.p_id=p.p_id
    JOIN orders o ON o.ord_id=oi.ord_id
    JOIN customers c ON c.cust_id=o.cust_id



SELECT * FROM billing_info;




-- HAVING CLAUSE---------------------------
SELECT p_name,sum(total_price) FROM
billing_info 
    GROUP BY (p_name)
    HAVING SUM(total_price) > 1500;    -- GROUP BY ke saath koi condition lgana ho toh WHERE ke badle HAVING use krna hoga


-- GROUP BY ROLLUP
SELECT 
    COALESCE(p_name,'Total'),
    sum(total_price) FROM billing_info
    GROUP BY 
    ROLLUP(p_name)
    ORDER BY sum(total_price);

   



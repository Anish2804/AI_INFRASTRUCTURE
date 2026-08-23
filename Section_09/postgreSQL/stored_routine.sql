-- stored routine:-An SQL statement or a set of SQL statements that can be stored on database server which can be call no. of times.

-- Types of Stored Routine: (1)Stored Procedure   (2)User Defined Function
CREATE OR REPLACE PROCEDURE update_emp_salary(
    p_employee_id INT,
    p_new_salary NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE employee
    SET salary = p_new_salary
    WHERE emp_id = p_employee_id;
END;
$$;

-- calling the procedure that we made 
CALL update_emp_salary(3,71000);        -- Alias jaisa kch smjh lo iss stored procedure ko

-- reading the table
SELECT * FROM employee;






-- USER DEFINED FUNCTION-------------------------------------------------------


-- QUERY:- Find name of the employees in each department having maximum salary.
-- Ek function bna diye bss jisko baar baar call kr skte h parameter use krke

CREATE OR REPLACE FUNCTION dept_max_sal_emp1(dept_name VARCHAR)
RETURNS TABLE(emp_id INT, fname VARCHAR, salary NUMERIC) 
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        e.emp_id,  e.fname, e.salary
    FROM 
        employee e
    WHERE 
        e.dept = dept_name
        AND e.salary = (
            SELECT MAX(emp.salary)
            FROM employee emp
            WHERE emp.dept = dept_name
        );
END;
$$ LANGUAGE plpgsql;


SELECT * FROM dept_max_sal_emp1('HR');
SELECT * FROM dept_max_sal_emp1('IT');
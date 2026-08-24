-- Triggers are special procedures in a database that automatically execute predefined actions in response to certain events on a specified table or view.

-- Use case: Create a Trigger so that If we insert/update negative salary in a table, it will be triggered and set it to 0.

SELECT * FROM employee;

CALL update_emp_salary(2,-52000);


CREATE OR REPLACE FUNCTION check_salary()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.salary < 0 THEN
        NEW.salary := 0;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER before_insert_salary
BEFORE UPDATE ON employee
FOR EACH ROW
EXECUTE FUNCTION check_salary();



-- ON DELETE CASCADE is a foreign key option in SQL.
-- It means:
-- If a parent row is deleted, automatically delete all related child rows.
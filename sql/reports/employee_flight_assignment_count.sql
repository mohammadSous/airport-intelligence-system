SELECT
    e.Emp_id AS employee_id,
    CONCAT(e.emp_first_name, ' ', e.emp_last_name) AS employee_name,
    e.emp_role,
    COUNT(a.flight_id) AS flights_assigned
FROM employee e
LEFT JOIN employee_assignment a 
    ON e.Emp_id = a.emp_id
GROUP BY e.Emp_id, e.emp_first_name, e.emp_last_name, e.emp_role
ORDER BY flights_assigned DESC;
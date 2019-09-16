SELECT
    *
FROM
    employee emp1
    INNER JOIN (
        SELECT
            department, max(salary) AS max_salary
        FROM
            employee
        GROUP BY
            department
    ) department_max_salaries
    ON emp1.salary = department_max_salaries.max_salary \
    AND emp1.department = department_max_salaries.department
ORDER BY
    department_max_salaries.max_salary DESC

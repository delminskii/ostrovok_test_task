SELECT
    emp1.department, emp1.name, emp1.salary
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
    department_max_salaries.max_salary DESC,
    name ASC,
    department ASC

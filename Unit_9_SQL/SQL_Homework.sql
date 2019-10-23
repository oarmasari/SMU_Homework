-- create tables and import data
CREATE TABLE departments (
    dept_no VARCHAR(10),
    dept_name VARCHAR(30)
);
CREATE TABLE dept_emp (
    emp_no INT,
    dept_no VARCHAR(10),
    from_date DATE,
    to_date DATE
);
CREATE TABLE dept_manager (
    dept_no VARCHAR(10),
    emp_no INT,
    from_date DATE,
    to_date DATE
);
CREATE TABLE employees (
    emp_no INT,
    birth_date DATE,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    gender VARCHAR(10),
    hire_date DATE
);
CREATE TABLE salaries (
    emp_no INT,
    salary INT,
    from_date DATE,
    to_date DATE
);
CREATE TABLE titles (
    emp_no INT,
    title VARCHAR(30),
    from_date DATE,
    to_date DATE
);
-- employee data with employee number, last name, first name, gender, and salary
SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary FROM employees AS e
JOIN salaries AS s ON e.emp_no=s.emp_no
ORDER BY emp_no;
-- employees hired in 1986
SELECT * FROM employees
WHERE EXTRACT(year FROM hire_date) = 1986
ORDER BY hire_date;
/*
manager data with  department number, department name, the manager's employee number,
last name, first name, and start and end employment dates
*/
SELECT m.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name, m.from_date, m.to_date FROM dept_manager AS m
JOIN departments AS d ON m.dept_no=d.dept_no
JOIN employees AS e ON m.emp_no=e.emp_no
ORDER BY dept_no;
-- employee data with employee number, last name, first name, and department name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees AS e
JOIN dept_emp ON e.emp_no=dept_emp.emp_no
JOIN departments AS d ON dept_emp.dept_no=d.dept_no
ORDER BY emp_no;
-- employees whose first name is "Hercules" and last names begin with "B"
SELECT * FROM employees
WHERE first_name='Hercules' AND last_name LIKE 'B%'
ORDER BY emp_no;
-- employees in the Sales department with employee number, last name, first name, and department name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees AS e
JOIN dept_emp ON e.emp_no=dept_emp.emp_no
JOIN departments AS d ON dept_emp.dept_no=d.dept_no
WHERE dept_name='Sales'
ORDER BY emp_no;
-- employees in the Sales and Development departments with employee number, last name, first name, and department name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees AS e
JOIN dept_emp ON e.emp_no=dept_emp.emp_no
JOIN departments AS d ON dept_emp.dept_no=d.dept_no
WHERE dept_name='Sales' OR dept_name='Development'
ORDER BY emp_no;
-- employees with same last name
SELECT last_name, count(last_name) AS num_occurance FROM employees
GROUP BY last_name
ORDER BY num_occurance DESC;
-- Epilogue: who am I? 499942
SELECT * FROM EMPLOYEES
WHERE emp_no=499942;
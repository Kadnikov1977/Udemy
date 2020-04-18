--CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);

--SELECT * FROM students;
--CREATE TABLE employees (first_name TEXT, last_name TEXT, age INTEGER);
--INSERT INTO employees (first_name, last_name, age) VALUES ('larisa', 'Kadnikova', 42);
--INSERT INTO employees (first_name, last_name, age) VALUES ('Igor', 'Kadnikov', 42);
--INSERT INTO employees (first_name, last_name, age) VALUES ('Vlad', 'Kadnikov', 20);
INSERT INTO employees (first_name, last_name, age) VALUES ('Dima', 'Kotelnikov', 38);
INSERT INTO employees (first_name, last_name, age) VALUES ('Natasha', 'Kotelnikova', 38);
INSERT INTO employees (first_name, last_name, age) VALUES ('Anton', 'Kotelnikov', 10);
--DROP TABLE students;

--SELECT first_name FROM employees;
--SELECT first_name,age FROM employees;

SELECT first_name, age FROM employees WHERE age > 21;
SELECT first_name, age FROM employees WHERE last_name LIKE 'Kadnikov%';
SELECT first_name, age FROM employees WHERE last_name LIKE '%ov' OR first_name LIKE '____';

UPDATE employees SET last_name = 'Кадников' WHERE last_name = 'Kadnikov';
UPDATE employees SET last_name = 'Кадникова' WHERE last_name = 'Kadnikova';

DELETE FROM employees WHERE age < 11;
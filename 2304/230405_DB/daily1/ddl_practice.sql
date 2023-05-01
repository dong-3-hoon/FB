CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
 );

 SELECT * FROM users;

 SELECT first_name, age, balance FROM users 
 ORDER BY age, balance DESC;

 SELECT first_name, age FROM users
 ORDER BY first_name, age DESC;
 
SELECT first_name, country FROM users
WHERE first_name='건우' AND country='경기도';

SELECT first_name, phone, country FROM users
WHERE phone LIKE '%-51__-%' AND country NOT IN('서울');

SELECT first_name, age FROM users
ORDER BY age ASC LIMIT 20 OFFSET 40;
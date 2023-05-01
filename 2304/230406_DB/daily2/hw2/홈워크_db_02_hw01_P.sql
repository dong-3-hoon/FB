CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 변수를 지정하지 않았는데 순서가 맞지 않아서 다르게 삽입된다.
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2) rowid를 선언하지 않았는데 삽입했다.
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);

-- 3) 필수 요소인 weight가 삽입되지 않았다.
INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);

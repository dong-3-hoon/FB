CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);
-- 무게 100이하인 동물 삭제
BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
-- ROLLBACK기 때문에 저장 X

BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;
-- onmivore를 주식으로 하는 동물을 삭제하고 COMMIT로 저장
-- 동물의 개수 출력
SELECT COUNT(*)
FROM zoo;

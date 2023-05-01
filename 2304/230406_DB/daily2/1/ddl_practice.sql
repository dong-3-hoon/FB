CREATE TABLE animals(
    animal_name TEXT NOT NULL,
    height INT NOT NULL,
    weight INT NOT NULL,
    age INT
);

SELECT * FROM animals;

ALTER TABLE animals 
ADD meal TEXT NULL;

ALTER TABLE animals
RENAME animal_name TO name;

ALTER TABLE animals
RENAME TO zoo;

DROP TABLE zoo;
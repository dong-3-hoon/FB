-- 테이블 생성
CREATE TABLE contacts(
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  eamil TEXT NOT NULL UNIQUE
);
--테이블 구조 변경: 이름 변경
ALTER TABLE contacts RENAME TO new_contacts;
--테이블 속성 이름 변경
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT "no address";

DROP TABLE new_contacts;
DROP TABLE contacts;
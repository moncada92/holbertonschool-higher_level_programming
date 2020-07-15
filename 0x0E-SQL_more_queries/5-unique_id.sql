-- create table default value field id and unique
-- user_0d_2 on your server (in localhost).
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
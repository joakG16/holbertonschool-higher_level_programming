-- Write a script that creates the table force_name on your MySQL server.
-- name can’t be null
CREATE TABLE IF NOT EXISTS force_name (
   id INT,
   name VARCHAR(256) NOT NULL
);

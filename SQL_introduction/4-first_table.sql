--  a script that creates a table called "first_table" in the current database in your MySQL server.
-- The database name will be passed as an argument of the mysql command, example:
-- "mysql -hlocalhost -uroot -p hbtn_0c_0" --> hbtn_0c_0 database pased 
-- inside paraenthesis, the column's name and its datatype wil be specified
CREATE TABLE IF NOT EXISTS first_table (
   id INT,
   name VARCHAR(256)
);

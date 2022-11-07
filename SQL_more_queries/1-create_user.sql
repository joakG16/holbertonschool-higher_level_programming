-- Writing a script that creates the MySQL server user user_0d_1.
-- The user_0d_1 password should be set to user_0d_1_pwd
-- IF the user user_0d_1 already EXISTS, your script should NOT fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

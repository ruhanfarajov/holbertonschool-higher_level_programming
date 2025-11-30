-- this is creating both the database and user if any of which does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE ON '*' TO 'user_0d_2'@'localhost';
GRANT SELECT  ON 'hbtn_0d_2' TO 'user_0d_2'@'localhost';

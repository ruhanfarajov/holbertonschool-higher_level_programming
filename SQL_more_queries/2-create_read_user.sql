-- this is creating both the database and user if any of which does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- 2. Create the user user_0d_2 safely without setting the password initially.
-- This prevents the common conflict error when combining IF NOT EXISTS and IDENTIFIED BY.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- 3. Set the user's password using ALTER USER.
-- This command will work whether the user was just created or already existed.
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- 4. Grant SELECT privileges on ALL tables in the hbtn_0d_2 database to the user.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- 5. Apply all permission changes immediately.
FLUSH PRIVILEGES;

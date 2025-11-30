--  this is my first join statement
USE hbtn_test_db_9

SELECT
	cities.id, cities.name, states.name
FROM
	cities 
JOIN
	states
ON
	cities.state_id = states.id
ORDER BY
	cities.id  ASC;

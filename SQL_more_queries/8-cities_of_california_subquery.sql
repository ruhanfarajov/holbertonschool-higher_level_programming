-- this script is my first filter in SQL
SELECT 
	cities.id,
	cities.name
FROM 
	cities,
	states
WHERE
	cities.state_id = states.id && states.name = 'California'
ORDER BY
	cities.id
	ASC

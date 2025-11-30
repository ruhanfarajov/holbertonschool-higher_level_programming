--  this is my first join statement

SELECT
	cities.id, cities.name, states.name
FROM
	cites 
JOIN
	states
ON
	cities.state_id = states.id

-- this counts evertying

SELECT
	score,
	COUNT(score) AS count_of_people
FROM
	second_table
GROUP BY
	score

-- this is showing full join everything

SELECT
        s.title, g.genre_id
FROM
        tv_shows AS s
LEFT JOIN
        tv_show_genres AS g
ON
        s.id =g.show_id 
ORDER BY
	s.titile, g.genre_id ASC;

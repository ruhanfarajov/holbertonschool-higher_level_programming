-- this is showing full join everything

SELECT
        s.title, g.genre_id
FROM
        tv_shows AS s
JOIN
        tv_show_genres AS g
ON
        s.id =g.show_id 

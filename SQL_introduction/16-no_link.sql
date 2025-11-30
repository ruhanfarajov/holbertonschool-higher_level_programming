-- this is doing the no link file  implmentation
SELECT score, name
FROM second_table
WHERE name IS NOT NULL;
ORDER BY score DESC

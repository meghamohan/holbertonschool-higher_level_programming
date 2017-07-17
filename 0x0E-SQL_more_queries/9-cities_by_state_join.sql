-- lists all cities in the database, using JOIN
SELECT c.id, c.name, s.name
FROM cities c
INNER JOIN states s on s.id = c.state_id
ORDER BY c.id ASC;

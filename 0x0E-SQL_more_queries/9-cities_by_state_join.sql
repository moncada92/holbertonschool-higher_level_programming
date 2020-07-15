-- select two tables join
-- user_0d_2 on your server (in localhost).
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
WHERE cities.state_id = states.id
-- Write a script that lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement

-- The INNER JOIN will only return the matching records when both of their id's match, that means the state_id
-- in the "cities" table need to match the states's id in the "states" table
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states on cities.state_id = states.id
ORDER BY cities.id;

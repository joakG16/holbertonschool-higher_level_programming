-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked

-- it will count the times the genre's name was repeated after matching its id with the other table
-- (which only exposes how many times a show identified with certain genre), and group it in one single record each

SELECT tv_genres.name AS genre, COUNT(*) AS 'number_of_shows'
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;

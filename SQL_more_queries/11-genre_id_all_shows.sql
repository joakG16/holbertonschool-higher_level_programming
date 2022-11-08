-- Write a script that lists ALL shows contained in the database hbtn_0d_tvshows.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

-- The left join will return every row or record on the left table(tv_shows) even when there's
-- no matching row in the right table(tv_show_genres) (nulls in right)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

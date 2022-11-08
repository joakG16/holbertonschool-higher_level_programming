-- Import the database dump from hbtn_0d_tvshows to your MySQL server and write a script that lists all shows contained in hbtn_0d_tvshows
-- that have AT LEAST one genre LINKED.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

-- Write a script that lists all shows contained in hbtn_0d_tvshows WITHOUT a genre linked.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

-- It's the same as the previous task, only that now the condition that sees if the show's genre id is NULL, is added
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

-- lists all shows contained in hbtn_0d_tvshows
-- user_0d_2 on your server (in localhost).
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title ASC, name ASC;
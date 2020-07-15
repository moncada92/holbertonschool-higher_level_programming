-- lists all shows contained in hbtn_0d_tvshows
-- user_0d_2 on your server (in localhost).
SELECT tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = "Dexter" ORDER BY name;
-- List all Comedy shows in 'hbtn_0d_tvshows'
-- 'tv_genres' table contains only one record where name = Comedy
-- Results must be sorted in ascending order by the show title
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres tsg ON tv_shows.id = tsg.show_id
INNER JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY tv_shows.title ASC;

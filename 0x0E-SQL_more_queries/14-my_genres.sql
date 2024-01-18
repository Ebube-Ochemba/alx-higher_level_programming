-- Use 'hbtn_0d_tvshows' to list all genres of show 'Dexter'
-- Each record should display tv_genres.name
-- Results must be sorted in ascending order by genre name
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres tsg ON tv_genres.id = tsg.genre_id
INNER JOIN tv_shows ts ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY tv_genres.name ASC;

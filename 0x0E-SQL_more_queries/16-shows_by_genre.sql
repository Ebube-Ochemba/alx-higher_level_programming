-- List all shows and genres linked to show from 'hbtn_0d_tvshows'
-- If show doesn't have a genre, display NULL in genre column
-- Each record should display tv_shows.title, tv_genres.name
-- Results must be sorted in ascending order by show title
SELECT tv_shows.title, tv_genres.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres g ON tsg.genre_id = tg.id
ORDER BY ts.title ASC;

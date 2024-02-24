# SQL - More queries

> This project was on more about SQL and SQL queries.

## Summary

I learnt about how to create a new MySQL user, how to manage privileges for a user to a database or table, what a `PRIMARY KEY` is, what a `FOREIGN KEY` is, how to use `NOT NULL` and `UNIQUE` constraints, how to retrieve datas from multiple tables in one request, what subqueries are and what `JOIN` and `UNION` are.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-privileges.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/0-privileges.sql): A script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).
- [x] [1-create_user.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/1-create_user.sql): A script that creates the MySQL server user `user_0d_1`.
	- If the user `user_0d_1` already exists, your script should not fail.
- [x] [2-create_read_user.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/2-create_read_user.sql): A script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
	- If the user `user_0d_2` already exists, your script should not fail.
- [x] [3-force_name.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/3-force_name.sql): A script that creates the table `force_name` on your MySQL server.
	- If the table `force_name` already exists, your script should not fail
- [x] [4-never_empty.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/4-never_empty.sql): A script that creates the table `id_not_null` on your MySQL server.
	- If the table `id_not_null` already exists, your script should not fail.
- [x] [5-unique_id.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/6-states.sql): A script that creates the table `unique_id` on your MySQL server.
	- If the table `unique_id` already exists, your script should not fail.
- [x] [7-cities.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/7-cities.sql): A  script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.
	- If the table `states` already exists, your script should not fail.
- [x] [6-states.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/6-states.sql): A script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.
	- If the table `cities` already exists, your script should not fail.
- [x] [8-cities_of_california_subquery.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql): A script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
- [x] [9-cities_by_state_join.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/9-cities_by_state_join.sql): A script that lists all cities contained in the database `hbtn_0d_usa`.
- [x] [10-genre_id_by_show.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/10-genre_id_by_show.sql): A script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.
- [x] [11-genre_id_all_shows.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/11-genre_id_all_shows.sql): A script that lists all shows contained in the database `hbtn_0d_tvshows`.
- [x] [12-no_genre.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/12-no_genre.sql): A script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
- [x] [13-count_shows_by_genre.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/13-count_shows_by_genre.sql): A script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
- [x] [14-my_genres.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/14-my_genres.sql): A script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.
- [x] [15-comedy_only.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/15-comedy_only.sql): A script that lists all Comedy shows in the database `hbtn_0d_tvshows`.
- [x] [16-shows_by_genre.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/16-shows_by_genre.sql): A script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.
- [ ] [100-not_my_genres.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/100-not_my_genres.sql): A script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`.
- [ ] [101-not_a_comedy.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/101-not_a_comedy.sql): A script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.
- [ ] [102-rating_shows.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/102-rating_shows.sql): A script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.
- [ ] [103-rating_genres.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/103-rating_genres.sql): A script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.

> [`hbtn_0d_tvshows`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/hbtn_0d_tvshows.sql); Database dump from `hbtn_0d_tvshows` to be imported to your __*MySQL server*__ and used for task 10 - 20.

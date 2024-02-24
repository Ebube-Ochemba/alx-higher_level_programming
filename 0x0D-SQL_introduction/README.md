# SQL - Introduction

> This project was an introduction to SQL.

## Summary

I learnt about Databases, relational databases, SQL and MySQL, how to create a database in MySQL, `DDL` and `DML`, how to `CREATE` or `ALTER` a table, how to `SELECT` data from a table, how to `INSERT`, `UPDATE` or `DELETE` data, subqueries and how to use MySQL functions.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-list_databases.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/0-list_databases.sql): A script that lists all databases of your MySQL server.
- [x] [1-create_database_if_missing.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/1-create_database_if_missing.sql): A script that creates the database `hbtn_0c_0` in your MySQL server.
	- If the database `hbtn_0c_0` already exists, your script should not fail.
- [x] [2-remove_database.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/2-remove_database.sql): A script that deletes the database hbtn_0c_0 in your MySQL server.
	- If the database `hbtn_0c_0` already exists, your script should not fail.
- [x] [3-list_tables.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/3-list_tables.sql): A script that lists all the tables of a database in your MySQL server.
- [x] [4-first_table.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/4-first_table.sql): A script that creates a table called `first_table` in the current database in your MySQL server.
	- If the table `first_table` already exists, your script should not fail.
- [x] [5-full_table.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/5-full_table.sql): A script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- [x] [6-list_values.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/6-list_values.sql): A script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- [x] [7-insert_value.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/7-insert_value.sql): A script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
- [x] [8-count_89.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/8-count_89.sql): A script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
- [x] [9-full_creation.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/9-full_creation.sql): A script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
- [x] [10-top_score.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/10-top_score.sql): A script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- [x] [11-best_score.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/11-best_score.sql): A script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- [x] [12-no_cheating.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/12-no_cheating.sql): A script that updates the score of Bob to `10` in the table `second_table`.
- [x] [13-change_class.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/13-change_class.sql): A script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- [x] [14-average.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/14-average.sql): A script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- [x] [15-groups.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/15-groups.sql): A script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- [x] [16-no_link.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/16-no_link.sql): A script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- [ ] [100-move_to_utf8.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/100-move_to_utf8.sql): A script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.
- [ ] [101-avg_temperatures.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/101-avg_temperatures.sql): A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
- [ ] [102-top_city.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/102-top_city.sql): A script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).
- [ ] [103-max_state.sql](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/103-max_state.sql): A script that displays the max temperature of each state (ordered by State name).

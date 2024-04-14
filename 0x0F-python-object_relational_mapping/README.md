# Python - Object-relational mapping

> This project was on Python ORMs.

## Summary

I learnt how to connect to a MySQL database from a Python script, how to `SELECT` rows in a MySQL table from a Python script, how to `INSERT` rows in a MySQL table from a Python script, what ORM means, how to map a Python Class to a MySQL table and how to create a Python Virtual Environment.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-select_states.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/0-select_states.py): A script that lists all `states` from the database `hbtn_0e_0_usa`.
- [x] [1-filter_states.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/1-filter_states.py): A script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`.
- [x] [2-my_filter_states.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/2-my_filter_states.py): A script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
- [x] [3-my_safe_filter_states.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py): A script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!
- [x] [4-cities_by_state.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/4-cities_by_state.py): A script that lists all `cities` from the database `hbtn_0e_4_usa`.
- [x] [5-filter_cities.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/5-filter_cities.py): A script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`.
- [x] [model_state.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/model_state.py): A python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.
- [x] [7-model_state_fetch_all.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/7-model_state_fetch_all.py): A script that lists all `State` objects from the database `hbtn_0e_6_usa`.
- [x] [8-model_state_fetch_first.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/8-model_state_fetch_first.py): A script that prints the first `State` object from the database `hbtn_0e_6_usa`.
- [x] [9-model_state_filter_a.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/9-model_state_filter_a.py): A script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.
- [x] [10-model_state_my_get.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/10-model_state_my_get.py): A script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`.
- [x] [11-model_state_insert.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/11-model_state_insert.py): Ascript that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
- [x] [12-model_state_update_id_2.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/12-model_state_update_id_2.py): A script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.
- [x] [13-model_state_delete_a.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/13-model_state_delete_a.py): A script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.
- [x] [14-model_city_fetch_by_state.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py): A  script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`.
- [x] [100-relationship_states_cities.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/100-relationship_states_cities.py): A script that creates the `State` "California" with the `City` "San Francisco" from the database `hbtn_0e_100_usa`.
  	- [relationship_city.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/relationship_city.py): An improvement on the file `model_city.py`.
	- [relationship_state.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/relationship_state.py): An improvement on the files `model_state.py`.
- [x] [101-relationship_states_cities_list.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/101-relationship_states_cities_list.py): A script that lists all `State` objects, and corresponding `City` objects, contained in the database `hbtn_0e_101_usa`.
- [x] [102-relationship_cities_states_list.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/102-relationship_cities_states_list.py): A script that lists all `City` objects from the database `hbtn_0e_101_usa`.

> - [test_files](https://github.com/Ebube-Ochemba/alx-higher_level_programming/tree/master/0x0F-python-object_relational_mapping/test_files): A folder of test files. Provided by Alx.

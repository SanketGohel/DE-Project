# Data Modeling with PostgreSQL
* A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their music streaming app.The analytics team is particulary interested in understanding what songs users are listening to. Currently, they don't have an easy way to do query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

* We created a Postgres database and ETL pipeline for this analysis with tables designed to optimize queries on song play analysis.


## Schema Design

### Fact Table

* songplay: Records in log data associated with song plays i.e records with page NextSong songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent.

### Dimension table

* users: user in the app user_id, first_name, last_name, gender, level.

* songs: songs in music database song_id, title_id, artist_id, duration.

* artist: artists in music database artist_id, name, location, latitude, longtiude.

* time: timestamps of record in songplay broken down into specific units start_time, hour, day, week, month, year, weekday.

### Scripts

* sql_quires.py - Includes (CRUD) quries.
* create_tables.py - Resets the database by creating and dropping tables.
* etl.py - loads the json files for songs and logs dataset from the data folder on the db in star schema structure.


### Steps to Run
1. python create.py
2. python etl.py

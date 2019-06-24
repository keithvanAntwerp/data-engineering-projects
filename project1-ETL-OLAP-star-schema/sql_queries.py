# DROP TABLES
#songplay_table_drop = "drop table if exists songplays"
#user_table_drop = "drop table if exists users"
#song_table_drop = "drop table if exists songs"
#artist_table_drop = "drop table if exists artists"
#time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (
songplay_id serial primary key,
start_time varchar(100),
user_id varchar(100),
level varchar(100),
song_id varchar(100),
artist_id varchar(100),
session_id varchar(100),
location varchar(100),
user_agent varchar(500)
);""")

user_table_create = ("""CREATE TABLE users (
user_id varchar(100) primary key,
first_name varchar(100),
last_name varchar(100),
gender varchar(100),
level varchar(100)
);""")

song_table_create = ("""CREATE TABLE songs (
song_id varchar(100) primary key,
title varchar(100),
artist_id varchar(100),
year integer,
duration real
)
""")

artist_table_create = ("""CREATE TABLE artists (
artist_id varchar(100),
name varchar(100),
location varchar(100),
latitude real,
longitude real
);
""")

time_table_create = (""" CREATE TABLE time (
start_time bigint primary key,
hour integer,
day integer,
week integer,
month integer,
year integer,
weekday integer
);
""")

# INSERT RECORDS
# when executing command make sure to
# cur.execute(SQL, data)
# data is protected from a SQL injection attack?

songplay_table_in1 = ("""INSERT INTO songplays (start_time,
    user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""")

user_table_in1 = (
"""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO NOTHING;
""")

song_table_in1 = ("""INSERT INTO songs (song_id, title, artist_id, year,
    duration) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;""")

artist_table_in1 = ("INSERT INTO artists (artist_id, name, location, \
    latitude, longitude) VALUES (%s, %s, %s, %s, %s);")

time_table_in1 = (
"""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT (start_time) DO NOTHING;
""")


# FIND SONGS
song_select = ("""
select songs.song_id, songs.artist_id
from songs inner join artists
on songs.artist_id = artists.artist_id
where lower(songs.title) = %s AND  lower(artists.name) = %s
AND (abs(songs.duration - %s) < 5);
""")

#song_select = ("""
#select *
#from songs inner join artists
#on songs.artist_id = artists.artist_id 
#where artists.name= %s AND songs.title = %s;
#""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create]
#drop_table_queries = [songplay_table_drop, user_table_drop,
#                     song_table_drop, artist_table_drop, time_table_drop]

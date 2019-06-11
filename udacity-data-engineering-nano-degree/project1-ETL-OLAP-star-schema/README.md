# Sparkify Project 1 Overview

Sparkify has deployed a music streaming app.
The Sparkify analytics team wants a **PostgreSQL**
database and ETL pipeline with a schema and flow  
optimized for song play analysis.

1. **Extract** data from 2 collections of *JSON* files (almost).
Local directory structure and paths are provided.

2. **Transform** data into a star schema optimized for songplay analysis

3. **Load** in to customized _PostgreSQL Version ?_ database.

## Specified Project Constraints and Schema

### songplays fact table: song play event data

* start time of event
* user id
* user level
* song id
* artist id
* session id
* user location
* user agent

### artists table

* artist_id from the _Million Song Dataset_
* artist geospatial origin information requested (where the artist is from)
  * latitude, longitude, location

### songs table

* song_id from the _Million Song Dataset_
* title
* artist_id from the _Million Song Dataset_
* year
* duration

### users table

* user id
* first name
* last name
* gender
* level

### time table

* timestamps are given in the JSON log data


* start time, hour, day, week, month, year, weekday

## Data Type Considerations

* explicit type validations
  * input source file format and encoding: `JSON`
    * _Python 3_ `str()`
    * _PostgreSQL_ `varchar`
  * number type considerations
    * integer
    * floating-point
    * precise numeric
  * datatime type considerations
    * 
  * other data type considerations
*minimize resource cost: `min{[time, FLOPS, ]}`

## Efficiency and Complexity 

* time
* computing
* process operations
* memory considerations
* other goals:
* security
* reliability
* adaptability

### 1. Create the PostgreSQL database

### 2. ETL (Extract, Transform, Load) pipeline

Transfer data from a directory of JSON files into Postgres database using Python 3

#### Extracting

> Bring forth from storage into working memory

#### Transforming

#### Loading

- transfers data from files in two local directors into these tables in Postgres using Python and SQL

### 3. Test

by running queries provided by Sparkify analytics team to compare to expected results

### COPY

- Alternative is to convert the JSON to CSV files that can be used in the PostgreSQL `COPY table_name...`

```
COPY table_name [ (column [, ...] ) ]
    FROM {'filename' |  STDIN}
    [ [ WITH ] ( option [, ...] ) ]
```

### Example Queries

some text

### Dates

JavaScript Date objects are represented by the number of milliseconds since midnight
January 1, 1970. When the Date object is instantiated, the timestamp is in local device time.



```javascript
var now = new Date()
```


```python
import datetime from datetime




```

class datetime.datetime
A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

What are some good options for a dashboard?

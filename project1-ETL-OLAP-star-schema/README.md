# ETL to PostgreSQL Star Schema

The purpose of this project is:

* Extract data from 2 sources: 

  1. **application log files** from a music streaming application
  2. **Million Song Dataset** subset representing a rich **"big data"** set

* Transform it into a star schema optimized for online analytics processing (**OLAP**)
  * with a specific star schema requested

* Load into a single instance of a **PostgreSQL** server.

This is essentially a mini data mart that stitches rich artist and song data from
[The Million Song Data Set](http://millionsongdataset.com/) to
simulated application event logs.

## Example 
```
>>> python create_tables.py
create_tables.py:33: UserWarning: About to attempt to drop to reset database sparkifydb
  warnings.warn(("About to attempt to drop to reset database sparkifydb"))
If you would like to proceed type YES: YES
>>> python etl.py
80 files found in example-data/song_data
1/80 files processed.
2/80 files processed.
.
.
.
80/80 files processed.
34 files found in example-data/log_data
1/34 files processed.
.
.
.
34/34 files processed.
TEST QUERY: SELECT * FROM songplays LIMIT 5;
[(1, '1542837407796', 'SOZCTXZ12AB0182364', 'AR5KOSW1187FB35FF4', '15', 'paid', '818', 'Chicago-Naperville-Elgin, IL-IN-WI', '"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"')]
```

## Specified Project Constraints and Schema

NOTE: The relations shown in the **entity relationship diagram (ERD)** are conveying the central table foreign key to primary key and is a schema specified in the project.

![data mart schema](https://github.com/keithvanAntwerp/data-engineering-projects/blob/master/sparkify1.png)


## TODO and Questions

### Encodings

This project provides the opportunity to deal with encoding challenges.

`bad_encoding = "R\u00c3\u0083\u00c2\u00b6yksopp"`

### Questions and Comments

**JSON**: Javascript Object Notation

+ When a file has the extension *.json, what assumptions are safe to make? 
  + UTF-8 encoded
  + Are text "stacks" of JSON in line with RFC, ECMA?
    + common on log files

+ Disadvantage of not using Pandas?
  + Pandas is better computationally optimized?

+ Advantage of not using Pandas?
  + Scalability, Avoid RAM constraints?


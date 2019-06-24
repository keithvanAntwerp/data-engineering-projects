# ETL to PostgreSQL Star Schema

The purpose of this project is to extract data from 2 sources: 

1. **application log files** from a music streaming application
2. **Million Song Dataset** subset representing a rich **"big data"** set

to transform it into a star schema optimized for online analytics processing (**OLAP**)
and loaded into a single instance of **PostgreSQL** server

This is essentially a mini data mart that stitches rich artist and song data from
[The Million Song Data Set](http://millionsongdataset.com/) to
simulated application event logs.

## Summary of Extract, Transform, Load: ETL flow

1. **Extract** data from 2 collections of *JSON* files. 

2. **Transform** data into an OLAP star schema optimized for songplay analysis.

3. **Load** in to customized _PostgreSQL Version ?_ database.

## Specified Project Constraints and Schema

NOTE: The relations shown in the **entity relationship diagram (ERD)** are conveying the central table foreign key to primary key and is a schematic constraint specified in the project.

![data mart schema](https://github.com/keithvanAntwerp/data-engineering-projects/blob/master/sparkify1.png)


### Example Queries
```
>>> python create_tables.py
>>> python etl.py

>>> example queries
```
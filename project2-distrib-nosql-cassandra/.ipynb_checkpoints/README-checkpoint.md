# Data Modeling NoSQL

NoSQL database design
denormalization
primary keys
clustering columns
WHERE clause

NoSQL, "NOT ONLY SQL", non-relational

* high availability
* high volume of data
* linear scalability
* low latency
* fast READ/WRITE

https://www.xenonstack.com/blog/nosql-databases/

## Distributed Databases

* Database scaled out horizontally, across nodes
* minimal or zero downtime requirments
* COPIES, COPIES, COPIES
* eventual consistency
  * milliseconds of inconsistency
  * "workarounds to prevent stale data"

https://docs.datastax.com/en/dse-planning/doc/
https://en.wikipedia.org/wiki/Eventual_consistency
https://docs.datastax.com/en/cassandra/3.0/cassandra/architecture/archTOC.html
https://www.tutorialspoint.com/cassandra/cassandra_architecture.htm
https://docs.datastax.com/en/cassandra/3.0/cassandra/dml/dmlIntro.html

## CAP Theorem

2 of 3 possible:

1. Consistency: Every read from the database gets the latest (correct) piece of data or ERROR
2. Availability
3. Partition Tolerance

NoSQL databases differences influence database design

Cassandra is designed for AP: Availibility and Partition Toleranceansweranswer

https://en.wikipedia.org/wiki/CAP_theorem
https://www.voltdb.com/blog/2015/10/22/disambiguating-acid-cap/

Cassandra 




## Apache Cassandra
  
> Apache Cassandra is an open source, distributed, decentralized, elastically
scalable, highly available, fault-tolerant, tuneably consistent, row-oriented
database, that bases its distribution design on Amazon's Dynamo and its data model
on Google's Bigtable. Created at Facebook, it is now used at some of the most popular
sites on the web.

_--Cassandra: The Definitive Guide. Distributed Data at Web Scale_


## Cassandra with Python

A Python wrapper and driver called "cassandra" allows one to run Apache Cassandra queries.

`pip install cassandra-driver`

1. Start with importing cassandra

```python
import cassandra
from cassandra.cluster import Cluster

cluster = Cluster(['IP ADDRESS of Cassandra instance'])
session = cluster.connect()

session.execute("""
CREATE KEYSPACE IF NOT EXISTS name_of_keyspace
WITH REPLICATION = 
{'class': 'SimpleStrategy, 'replication_factor''}


session.set_keyspace('name_of_keyspace')
```

2. Music Library
  * return every album in the music library that was released in a given year
`select * from music_library where year = 1970`

  * return every album in the music library that was created by a given artist
`select * from artist_library where artist_name = "The Beatles"`

  * return all information from the music library about a given album
`select * from artist_library where album_name = "Close To You"`

denormalization

2 different queries -> 2 different tables!

partition key
clustering column

partition key

DENORMALIZE! Think about your queries first! No Joins in Cassandra!

Migrating from relational to Cassandra? Must transform! Denormalize! 

Apache Cassandra optimized for fast writes.

Usually, denormalized tables are slow for writes. OLTP are typically relational and 3NF.

https://docs.datastax.com/en/dse/6.7/cql/cql/ddl/dataModelingApproach.html

# project1-etl-olap-star-schema

A music streaming company Sparkify has deployed a music streaming app.
The analytics team wanted a **PostgreSQL**
OLAP database schema and ETL pipeline optimized for song play analysis.

This is essentially a mini data mart that links artist and song data from
[The Million Song Data Set] (http://millionsongdataset.com/) to
simulated application event logs.

## Summary of Extract, Transform, Load: ETL flow

1. **Extract** data from 2 collections of *JSON* files. 

2. **Transform** data into an OLAP star schema optimized for songplay analysis.

3. **Load** in to customized _PostgreSQL Version ?_ database.

## Specified Project Constraints and Schema

![data mart schema](https://github.com/keithvanAntwerp/data-engineering-projects/blob/master/sparkify1.png)

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

### Example Queries

some text

### Dates

JavaScript Date objects are represented by the number of milliseconds since midnight
January 1, 1970. When the Date object is instantiated, the timestamp is in local device time.

```javascript
var now = new Date()
```

(http://www.ee.columbia.edu/~dpwe/pubs/McFeeBEL12-MSDC.pdf) to the simulated log files.
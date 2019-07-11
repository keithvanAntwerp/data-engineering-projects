# A Reference for Database Management Systems

## PostgreSQL

### Constraints 

https://www.postgresql.org/docs/9.4/ddl-constraints.html

data type constraints

#### **Not-Null constraints**

```
CREATE TABLE table_name (
    col_name1 integer NOT NULL,
    col_name2 text NOT NULL,
    col_name3 numeric
);
```
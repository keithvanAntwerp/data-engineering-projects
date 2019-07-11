import psycopg2
import sys
import warnings
from sql_queries import create_table_queries #drop_table_queries              


def create_database():
    '''Return a psycopg2.connect() and psycopg2.cur() to a newly created 
    relational database with the aim of good exception handling.
    '''
    # connect to default database hosted locally
    try:
        conn = psycopg2.connect(
        "host=127.0.0.1 dbname=studentdb user=keithvanantwerp password = student")
    except psycopg2.Error as e:
        print(("ERROR: Could not connect to a default "
               "Postgres through psycopg2.connect()!"))
        print(("Recommend checking input to psycopg2.connect(input) (LINE 14), "
               "Postgres server status"))
        print("psycopg2 says: " + str(e))
        print("Exiting via sys.exit(), Goodbye.")
        sys.exit() #exit back to command line
    else: conn.set_session(autocommit=True)
    
    # establish cursor
    try: 
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("ERROR: unable to get cursor")
        print("psycopg2: " + str())
    
    # create sparkify database with UTF8 encoding
    warnings.warn(("About to attempt to drop to reset database sparkifydb"))
    if input("If you would like to proceed type YES: ") == 'YES':
        
        try:
            cur.execute("DROP DATABASE IF EXISTS sparkifydb")
            cur.execute(("CREATE DATABASE sparkifydb "
                         "WITH ENCODING 'utf8' TEMPLATE template0"))
    
        except psycopg2.Error as e:
            print("Error: Unable to execute DROP db or CREATE db")
            print(e)

    else: 
        print("User Abort: Not OK to drop database sparkifydb")
        sys.exit()
        
    # close connection to default database
    conn.close()

    # connect to sparkify database
    try:
        conn = psycopg2.connect(
            "host=127.0.0.1 dbname=sparkifydb user=student password=student")
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("ERROR: Could not connect to new sparkifydb")
        print(e)
    
    

    return cur, conn


#def drop_tables(cur, conn):
#    '''
#    '''
#    for query in drop_table_queries:
#        cur.execute(query)
#        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()

    #drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()

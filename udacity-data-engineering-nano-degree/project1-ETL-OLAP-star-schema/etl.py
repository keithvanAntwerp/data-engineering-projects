import os
import glob
import json as js
import psycopg2
from psycopg2 import sql
#import pandas as pd
import datetime

#custom import
from sql_queries import *

def get_json_files(dirpath):
    '''Return a list of full local paths
    of all files with *.json extension
    at or below this path
   
    '''
    all_files = []
    for root, _, files in os.walk(dirpath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    
    return all_files

def process_song_file(cur, filepath):
    '''Open a JSON file, load into Python as dict,
    insert into postgresql database
    '''
    # open song file
    with open(filepath) as jf:
        song_dict =js.load(jf)
    
    #neededKeys = ['artist_id', 'artist_latitude', 'artist longitude', 
    #              'artist_location']
    # insert song record
    song_data = [song_dict['song_id'], song_dict['title'], song_dict['artist_id'],
                 song_dict['year'], song_dict['duration']]
    
    cur.execute(song_table_in1, song_data)
    
    # insert artist record
   
    artist_data = [song_dict['artist_id'], song_dict['artist_name'], 
                   song_dict['artist_location'], song_dict['artist_latitude'], 
                   song_dict['artist_longitude']]
    
    cur.execute(artist_table_in1, artist_data)


def process_log_file(cur, filepath):
    '''
    Process a log file consisting of lines of JSON
    common in application logs.
    '''
    # open log file
    with open(filepath) as f:
        liStr = f.readlines()
    
    hiddenJSON = []

    for jsonStr in liStr:
        hiddenJSON.append(js.loads(jsonStr))

    neededKeys = ['artist', 'gender', 'location', 'firstName',
                  'lastName', 'ts', 'userAgent', 'sessionId',
                  'level', 'userId', 'song', 'length']
    
    # filter by NextSong action
    filteredJSON = []
    for temp_dict in hiddenJSON:
        if temp_dict['page'] == 'NextSong':
            filteredDict = { akey: temp_dict[akey] for akey in neededKeys }
            filteredJSON.append(filteredDict)
    
    for jf in filteredJSON: 
        #print(jf['ts'])
        tempdt = datetime.datetime.fromtimestamp(jf['ts']/1000)
        #insert time data
        cur.execute(time_table_in1, (jf['ts'], tempdt.hour, tempdt.day, tempdt.strftime("%W"),
                                     tempdt.month, tempdt.year, tempdt.weekday()))
        #insert user data
        cur.execute(user_table_in1, (jf['userId'], jf['firstName'], jf['lastName'], jf['gender'], jf['level']))
        #cur.execute()


    # insert songplay records

    # a song version can be approximately well-identified
    # by the artist who performed it. But artists play/record
    # same songs often as different versions
    # e.g. "LIVE" versions where you can hear all the fans cheering and you think
    # this band MUST be GREAT!

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (jf['song'].lower(),jf['artist'].lower(),jf['length']))
        #print(song_select, (jf['song']))
        results = cur.fetchall()
        #print(results)
        
        if results: #if not None
            print(results, type(results))
            song_play_data = [jf['ts'], results[0][0], results[0][1], 
                              jf['userId'], jf['level'], jf['sessionId'],
                              jf['location'], jf['userAgent']]
            cur.execute(songplay_table_in1, song_play_data)
       #else: 
            #song_play_data = [jf['ts'], None, None,
            #                  js['userId'], jf['level'], jf['sessionId'],
            #                  js['location'], js['userAgent']]
            
    
        #else: print(results)
            #songid, artistid = results
            #print(songid, artistid)
        #else: 
        #print(bool(results))
            #print(results, type(results))
    #   songid, artistid = results if results else None, None

        # insert songplay record
    #    songplay_data = []
    #    cur.execute(songplay_table_in1, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = get_json_files(filepath) #list of .json file paths
    
    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))
    #################################
    #### iterate over files and process#####
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))
    ########################################
def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb")
    cur = conn.cursor()
    print("f0")

    process_data(cur, conn, filepath='exampe-data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='example-data/log_data', func=process_log_file)

    conn.close()



if __name__ == "__main__":
    main()

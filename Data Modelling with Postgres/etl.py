import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    This function processes the song dataset and extracts the song and the artist data
    -----------
    cur:cursor
    filepath:path_to_song_file
    """
    # open song file
    df = 

    # insert song record
    song_data = 
    # insert artist record
    artist_data = 

def process_log_file(cur, filepath):
    """
    This Function processes the log dataset
    and extracts the time and the user info and records the activity in the songplay table
    ----------
    cur:cursor
    filepath:path_to_log_file
    """
    # open log file
    df =

    # filter by NextSong action
    df =

    # convert timestamp column to datetime
    t = 

    # insert time data records
    time_df = 


    # load user table
    user_df = 

    # insert user records
    
    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        # print(row.song, row.artist, row.length)
        cur.execute()
        results = cur.fetchone()
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = 


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()

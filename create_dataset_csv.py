import pandas as pd
import numpy as np
import json
import sys
import csv
import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Script to extract tweet IDs from the given dataset in Hydrator compatible format.')
    parser.add_argument('-f', action="store", dest="filename" , help="Enter the name of the csv file to rehydrate")
    results = parser.parse_args()

    fileN = results.filename
    #print(fileN[:-15])
    outputfile = fileN[:-15] + "_complete.csv"
    
    with open(fileN, 'r') as f , open(outputfile, mode='w') as tweet_csv :
        print("Data Extraction in progress...")
        tweet_writer = csv.writer(tweet_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        tweet_writer.writerow(['created_at', 'month', 'date', 'time', 'day','tweet_id', 'country','coordinates', 'full_text', 'language', 'retweet_count', 'favourite_count', 'reply_count'])

        for cnt, line in enumerate(f):
            try:
                tweet = json.loads(line) # load it as Python dict
            except:
                continue
            
            try :
                created_at = (tweet['created_at'])
                month =(tweet['created_at'].split(' ')[1])
                date = (tweet['created_at'].split(' ')[2])
                time = (tweet['created_at'].split(' ')[3])
                day = (tweet['created_at'].split(' ')[0])
            except :
                continue

            try :
                tweet_id =(tweet['id_str'])
            except:
                continue

            try :
                country = tweet['place']['country']
                
            except:
                continue

            try :
                coordinates = tweet['coordinates']
                print(coordinates)
                break
            except:
                coordinates = 'none'

            try :
                full_text = tweet['full_text']
            except:
                continue

            try :
                language = tweet['lang']
            except:
                language = 'none'

            try :
                retweet_count = tweet['retweet_count']
            except:
                retweet_count = 'none'

            try :
                favourite_count = tweet['favourite_count']
            except:
                favourite_count = 'none'

            try :
                reply_count = tweet['reply_count']
            except:
                reply_count = 'none'

            tweet_writer = csv.writer(tweet_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            tweet_writer.writerow([created_at, month, date, time, day, tweet_id, country, coordinates, full_text, language, retweet_count, favourite_count, reply_count])
    
    print("Data extracted!")
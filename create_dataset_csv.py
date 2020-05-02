import pandas as pd
import numpy as np
import json
import sys
import csv
import argparse
import os
import joblib

def extract_data(input_file) :
    outputfile = input_file[:-6] + "_complete.csv"
    regions = ['united states' , 'india', 'singapore' , 'united kingdom']
    usa_states = joblib.load('us_states.pkl')
    ind_states = joblib.load('indian_states.pkl')
    uk_counties = joblib.load('uk_counties.pkl')
    sgp_dist = joblib.load('sgp_dist.pkl')
    
    with open(input_file, 'r') as f , open(outputfile, mode='w') as tweet_csv :
        print("Data Extraction in progress... for file " + input_file)
        tweet_writer = csv.writer(tweet_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        tweet_writer.writerow(['created_at', 'month', 'date', 'time', 'day','tweet_id', 'country', 'location','coordinates', 'full_text', 'language', 'retweet_count', 'favourite_count', 'reply_count'])

        for cnt, line in enumerate(f):
            region_flag = 0 
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
                country = tweet['place']['country'].lower()
                
            except:
                country = 'none'
            
            try :
                location = 'none'
                l = tweet['user']['location']
                l = l.lower()
                temp = l.split(',')
                for i in temp :
                    if(i in usa_states) :
                        location = 'united states'
                        break 
                    elif(i in sgp_dist) :
                        location = 'singapore'
                        break
                    elif(i in uk_counties) :
                        location = 'united kingdom'
                        break
                    elif(i in ind_states) :
                        location = 'india'
                        break
                        
            except :
                location = 'none'
                    
            if(country in regions) :
                region_flag+=1
            if(location in regions) :
                region_flag+=1
            
            if(region_flag == 0) :
                continue
                
            try :
                coordinates = tweet['coordinates']
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
                
            if(language != 'en') :
                continue

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
            tweet_writer.writerow([created_at, month, date, time, day, tweet_id, country, location, coordinates, full_text, language, retweet_count, favourite_count, reply_count])

    print("completed!")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Script to extract tweet IDs from the given dataset in Hydrator compatible format.')
    parser.add_argument('-d', action="store", dest="dir" , help="Enter the directory containing the .jsonl files")
    results = parser.parse_args()

    directory = results.dir
    
    to_be_converted = []
    for _,_, files in os.walk(directory) :
        for f in files :
            ext = f.split('.')[-1]
            if(ext=='jsonl') :
                to_be_converted.append(f)
    
    for f in to_be_converted :
        extract_data(f)
    
    print("Script Execution Complete!")
# tweet_analysis
Contains scripts to extract tweet ID in hydrator compatible format and to extract desired fields from the hydrated .jsonl file

# Instructions for execution
* First download the clean dataset for a particular date.(Clean dataset does not contain retweets)
* Move the `<filename>.tsv` to the project directory.
* To extract tweet IDs in hydrator compatible format execute `python3 id_extractor.py -m 0 -f <filename>`
* This we return a .csv file containing just the tweet IDs with no headers and indices. `<filename>_tweetids.csv`
* This file can be passed as input to the hydrator.
* After Hydration is complete, save the .jsonl file in the same directory.
* To extract fields from the .jsonl file execute `python3 create_dataset_csv.py -f <filename>`
* This will return the csv file with the appropriate fields as `<filename>_complete.csv`

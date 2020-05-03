# tweet_analysis
Contains scripts to extract tweet ID in hydrator compatible format and to extract desired fields from the hydrated .jsonl file

# Instructions for execution (for id_extractor.py)
* First download the clean dataset for a particular date.(Clean dataset does not contain retweets)
* Move the `<filename>.tsv` to the project directory.
* To extract tweet IDs in hydrator compatible format execute `python3 id_extractor.py -m 0 -f <filename>`
* This we return a .csv file containing just the tweet IDs with no headers and indices. `<filename>_tweetids.csv`
* This file can be passed as input to the hydrator.
* After Hydration is complete, save the .jsonl file in the same directory.

# Instructions for execution (for create_dataset_csv.py)
* Create a folder conatining all the `.jsonl` files.
* Copy the contents of this repository in that same folder (do not miss the __.pkl__ files as they contain country related data.)
* To execute the script for the entire folder type: `python3 create_dataset_csv.py -d ./ `
* This will create the required csv files with the name `<filename>_complete.csv`

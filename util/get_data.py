import argparse
import os
import shutil
import sys
import json

parser = argparse.ArgumentParser(description='Download all relevant data for few shot prediction')
parser.add_argument('-c', '--credentials_file', help='Path to kaggle JSON credentials file.', required=True)
parser.add_argument('-f', '--force_refresh', help='Deletes existing data and refreshes if flag is set.', action="store_true")
args = parser.parse_args()

with open(args.credentials_file, 'r') as file:
    data = json.load(file)
    os.environ['KAGGLE_USERNAME'] = data['username']
    os.environ['KAGGLE_KEY'] = data['key']

# This authenticates on import so it needs to be down here after we already loaded in the creds from the file
import kaggle

# Looks weird but basically get the path for this script, then check if the ../data directory exists relative to this script
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "data")

# Make the directory if it doesn't already exist. If --force is specified, delete the directory and it's contents and recreate it
if os.path.exists(data_path):
    if not args.force_refresh:    
        print("./data already exists, skipping download. If you want to delete the data directory and redownload assets, you can run again with the -f flag.")
        sys.exit(1)
    shutil.rmtree(data_path)
os.makedirs(data_path)

print("Downloading datasets")
kaggle.api.dataset_download_files(
    "cjinny/mura-v11",
    path=os.path.join(data_path, "mura"),
    unzip=True,
    quiet=False,
)
kaggle.api.dataset_download_files(
    "bmadushanirodrigo/fracture-multi-region-x-ray-data",
    path=os.path.join(data_path, "fractures_target"),
    unzip=True,
    quiet=False,
)


"""Download data from our server
"""

# Global Variables
SERVER_URL = "http://icarus.cs.weber.edu/~hvalle/cs4580/data/"
FILE_NAME = "movies.csv"
KAGGLE_DATASET_NAME = ""

import os
import requests
import argparse
from zipfile import ZipFile, is_zipfile
# import kaggle

# TODO: Create another function to download the files 
# from Kaggle directly by passing the dataset name
def download_kaggle_data(dataset_name):
    """Downloads a dataset from Kaggle.

    Args:
        dataset_name (str): Name of the Kaggle dataset to download.
    """

    # Authenticate using the Kaggle API
    kaggle.api.authenticate()

    # Download the dataset
    kaggle.api.dataset_download_files(dataset_name, path='data', unzip=True)
    print(f"Kaggle dataset downloaded and unzipped successfully: {dataset_name}")

def download_file(url, file_name):
    """Downloads a file from a URL and optionally unzips it if it is a ZIP file.

    Args:
        url (str): URL of the file to download.
        file_name (str): Name of the file to download from the url
    """
    # Download the file
    url = (
        url + file_name
    )  # Append file name to url to get the download the actual file instead of the HTML page
    response = requests.get(url)

    if response.status_code == 200:
        # Save the file to the current working directory
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully: {file_name}")

        # Check if the file is a ZIP file, if True unzips the downloaded file into the 'data' directory
        if is_zipfile(file_name):
            unzip_file(file_name)
    else:
        print(f"Failed to download file. Status code: {response.status_code}")


def unzip_file(file_name):
    """Unzips a ZIP file, then removes the zipfile from the pwd after successful extraction

    Args:
        file_name (str): Name of the ZIP file to unzip.
    """
    with ZipFile(file_name, "r") as zip_ref:
        # Extract all the contents to the data directory
        zip_ref.extractall('data')
        print(f"File unzipped successfully: {file_name}")
        # Print all the names of the files extracted
        for file in zip_ref.namelist():
            print(f"Extracted: {file}")
    os.remove(file_name)


def main():
    """Driven function"""
    parser = argparse.ArgumentParser(description="Download data from a server.")
    parser.add_argument('--server_url', type=str, default=SERVER_URL, help='URL of the server to download data from')
    parser.add_argument('--file_name', type=str, default=FILE_NAME, help='Name of the file to download')
    args = parser.parse_args()

    download_file(args.server_url, args.file_name)


if __name__ == "__main__":
    main()

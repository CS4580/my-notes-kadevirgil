"""Download data from our server
"""

# Global Variables
SERVER_URL = "http://icarus.cs.weber.edu/~hvalle/cs4580/data/"
FILE_NAME = "plottingDemo01.zip"
KAGGLE_DATASET_NAME = ""

import os
import requests
from zipfile import ZipFile, is_zipfile

# TODO: Crate another function to download the files 
# frome kaggle directly by passing the dataset name
def download_kaggle_data(dataset_name): 
    pass

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

        # Check if the file is a ZIP file, if True unzippes the download file into the pwd
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
    os.remove(file_name)


def main(server_url, file_name):
    """Driven function"""
    download_file(server_url, file_name)


if __name__ == "__main__":
    main(SERVER_URL, FILE_NAME)

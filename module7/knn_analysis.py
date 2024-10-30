""" KNN Analaysis of Movies"""

import pandas as pd
import numpy as np

# Constants
K = 10 # Number of closest neighbors to consider
BASE_CASE_ID = 88763 # IMDB_id to use as base case (Back to the Future)


def knn_analysis_driver(df, base_case_id, comparison_type, metric_stub, sorted_value='metric'):
    # WIP: Create df of filter data
    df[sorted_value] = df[comparison_type].map(lambda x: metric_stub(base_case_id[comparison_type], x))


def main():
   """ Driven function """
   df = pd.read_csv('data/movies.csv')
   print(f'Dataset columns: {df.columns}')
   print(f'Dataset description: {df.describe()}')

if __name__ == "__main__":
    main()


#import autonormalize
import dfstools as dt
import featuretools as ft
import sys
import click
import os
import pandas as pd


def save_demo_data(es, file_list):
    for f in file_list:
        file_with_path = os.path.join('data', os.path.join(f, f + '.csv'))
        print(f'Saving {f} to {file_with_path}')
        es[f].df.to_csv(file_with_path, index=False)


def download_data():
    # check to see if data is already downloaded
    file_list = ['trip_logs', 'flights', 'airlines', 'airports']

    # If any file in the list is missing, download and save them all
    for f in file_list:
        file_with_path = os.path.join('data', os.path.join(f, f+'.csv'))
        if not os.path.exists(file_with_path):
            if click.confirm('OK to download demo featuretools data?', default=False):
                es = ft.demo.load_flight(verbose=True)
                save_demo_data(es, file_list)
                break


# demonstration - this will be removed later
if __name__ == "__main__":

    print(sys.version)
    print(sys.executable)

    # Download example data (if it doesn't exist)
    download_data()

    dataframe_dict = {'airlines': pd.read_csv(os.path.join('data', 'airlines', 'airlines.csv')),
                      'flights': pd.read_csv(os.path.join('data', 'flights', 'flights.csv')),
                      'airports': pd.read_csv(os.path.join('data', 'airports', 'airports.csv'))}

    print(dt.load_csv_to_df(None))

    relationship_dict = dt.get_dataset_dtypes(None)
    print(relationship_dict)

    relationship_dict = dt.find_primary_key_candidates(None, relationship_dict)
    print(relationship_dict)

    relationship_dict = dt.find_related_cols_by_name(dataframe_dict, relationship_dict)
    # print('standard relationship dict unfiltered for relationships: ')
    print(relationship_dict)

    relationship_dict = dt.find_parent_child_relationships(None, relationship_dict)
    print(relationship_dict)

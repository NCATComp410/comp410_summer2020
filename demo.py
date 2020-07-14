#import autonormalize
import dfstools as dt
import featuretools as ft
import sys
import click
import os
import pprint

pp = pprint.PrettyPrinter(width=41, compact=True)


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
    # Show current system information
    print(sys.version)
    print(sys.executable)

    # Download example data (if it doesn't exist)
    download_data()

    # Load the csv files into dataframes
    print('=================')
    print('Loading CSV Files')
    dataframe_dict = dt.load_csv_to_df('data',
                                       include_hidden=False,
                                       traverse_subdir=True,
                                       ignore_errors=True,
                                       follow_symlink=False)
    print('Found the following tables:')
    print(dataframe_dict.keys())

    print('================')
    print("get datatypes...")
    relationship_dict = dt.get_dataset_dtypes(dataframe_dict)
    pp.pprint(relationship_dict)

    print('===================')
    print("get primary keys...")
    relationship_dict = dt.find_primary_key_candidates(dataframe_dict, relationship_dict)
    pp.pprint(relationship_dict)

    print('===============================')
    print('Finding related columns by name')
    relationship_dict = dt.find_related_cols_by_name(dataframe_dict, relationship_dict)
    # print('standard relationship dict unfiltered for relationships: ')
    pp.pprint(relationship_dict)

    print('===============================')
    print('Find related columns by content')
    relationship_dict = dt.find_related_cols_by_content(dataframe_dict, relationship_dict)
    pp.pprint(relationship_dict)

    print('==================================')
    print("find parent child relationships...")
    relationship_dict = dt.find_parent_child_relationships(dataframe_dict, relationship_dict)
    pp.pprint(relationship_dict)

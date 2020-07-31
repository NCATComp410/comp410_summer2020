import pandas as pd
import os

# Prints aggie pride message
def show_aggie_pride():
    print('Aggie Pride - Worldwide')

def find_csv_files(path, include_hidden, traverse_subdir, follow_symlink):
    file_list = []
    #if traverse_subdir ==  false
    if not traverse_subdir:
        for dirpath, dirname, files in os.walk(path):
            for name in files:
                if name.endswith('.csv'):
                    file_list.append(os.path.join(path, name))
    # if traverse_subdir ==  True
    else:
        for dirpath, dirname, files in os.walk(path):
            for name in files:
                if include_hidden:
                    if name.startswith('.'):
                        print(name + ' is hidden!')
                if name.endswith('.csv'):
                    file_list.append(os.path.join(dirpath, name))
    return file_list

def dataframes_from_file_list(file_list: list, ignore_errors: bool) -> dict:
    # data structure to be returned
    dataframe_dict = {}

    # loop through each file in path
    for file in file_list:
        # display which file is being loaded
        print('Loading ' + file)

        # get the name of the file without the
        # .csv extension.  Use this as an index
        # in the return dict
        file_name = os.path.splitext(os.path.basename(file))[0]

        # attempt to read the dataframe
        try:
            dataframe_dict[file_name] = pd.read_csv(file)
        except (pd.errors.ParserError, pd.errors.EmptyDataError) as e:
            # if ignore_errors == True display a message
            # and continue processing
            if ignore_errors:
                print('Ignoring Error file not loaded: ' + file)
                print(e)
            # if else throw an exception
            else:
                print('ParseError file not loaded: ' + file)
                raise e

    # return the dataframes
    return dataframe_dict

def load_csv_to_df(path, include_hidden=False, traverse_subdir=True, follow_symlink=False, ignore_errors=False):
    file_list = find_csv_files(path, include_hidden, traverse_subdir, follow_symlink)
    return dataframes_from_file_list(file_list, ignore_errors)

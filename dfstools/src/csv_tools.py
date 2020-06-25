import pandas as pd


# Prints aggie pride message
def show_aggie_pride():
    print('Aggie Pride - Worldwide')


def load_csv_to_df(path, include_hidden=False, traverse_subdir=True, follow_symlink=False, ignore_errors=False):
    # path
    #    Starting path location to begin search
    #
    # include_hidden
    #     True  = Include any hidden files found while searching
    #     False = Ignore hidden files
    #
    # traverse_subdir
    #     True  = Traverse into any sub-directories found in <path>
    #     False = Do not traverse sub-directories
    #
    # follow_symlink
    #     True  = Follow any symbolic links
    #     False = Do not follow symbolic links
    #
    # ignore_errors
    #    False = Throw exception whenever an error is encountered
    #    True  = Print error message but continue processing


    ###
    # Student code (create additional functions as necessary)
    ###

    # mock-up for demonstration - remove after development
    #dataframe_list = ['airlines', 'airports', 'flights', 'trip_logs']
    dataframe_dict = {'airlines': pd.read_csv('data/airlines/airlines.csv'),
                      'flights': pd.read_csv('data/flights/flights.csv'),
                      'airports': pd.read_csv('data/airports/airports.csv'),
                      'trip_logs': pd.read_csv('data/trip_logs/trip_logs.csv')}
    # Return a list of pandas dataframe objects

    return dataframe_dict

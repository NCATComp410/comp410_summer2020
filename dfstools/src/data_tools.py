import pandas as pd

def get_dataset_dtypes(dataframe_list):
    # dataframe_list
    #     List of pandas dataframe objects

    ###
    # Student code (create additional functions as necessary)
    ###

    # mock-up for demonstration - remove after development
    # this is only a partial column list
    # actual list will come from columns in each dataframe
    relationship_dict = {'airlines': {},
                         'airports': {},
                         'flights': {},
                         'trip_logs': {}}

    relationship_dict['airlines']['carrier'] = {'dtype':'O'}
    relationship_dict['airports']['dest'] = {'dtype': 'O'}
    relationship_dict['flights']['dest'] = {'dtype': 'O'}
    relationship_dict['flights']['carrier'] = {'dtype': 'O'}
    relationship_dict['flights']['flight_id'] = {'dtype': 'O'}
    relationship_dict['trip_logs']['flight_id'] = {'dtype': 'O'}

    # return relationship structure
    return relationship_dict


def find_primary_key_candidates(dataframe_list, relationship_dict=None):
    # dataframe_list
    #     List of pandas dataframe objects
    #
    # relationship_dict
    #     This is an existing relationship_dict.  If None, a new
    #     relationship_dict should be created


    ###
    # Student code (create additional functions as necessary)
    ###

    # mock-up for demonstration - remove after development
    relationship_dict['airlines']['carrier']['key_candidate'] = True
    relationship_dict['airports']['dest']['key_candidate'] = True
    relationship_dict['flights']['dest']['key_candidate'] = False
    relationship_dict['flights']['carrier']['key_candidate'] = False
    relationship_dict['flights']['flight_id']['key_candidate'] = True
    relationship_dict['trip_logs']['flight_id']['key_candidate'] = False

    # return relationship structure
    return relationship_dict

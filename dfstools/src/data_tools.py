import pandas as pd


def get_dataset_dtypes(dataframe_list):
    # dataframe_list
    #     List of pandas dataframe objects

    # For testing purposes if not passing a dataframe_list
    # return a default testing values
    if dataframe_list is None:
        return {'airlines': {'carrier': {'dtype': 'O'}},
                'airports': {'dest': {'dtype': 'O'}},
                'flights': {'dest': {'dtype': 'O'}, 'carrier': {'dtype': 'O'},'flight_id': {'dtype': 'O'}},
                'trip_logs': {'flight_id': {'dtype': 'O'}}}

    # Initialize the relationship structure
    relationship_dict = {}

    # Traverse through each table contained in the dataframe_list
    for table in dataframe_list:
        # Add this table to the relationship_dict
        relationship_dict[table] = {}

        # Traverse through each column in this table
        for col in dataframe_list[table].columns:
            # Add the column's dtyp to the relationship_dict
            relationship_dict[table][col] = {'dtype': str(dataframe_list[table][col].dtype)}

    # return final relationship structure
    return relationship_dict


def find_primary_key_candidates(dataframe_list, relationship_dict=None):
    # dataframe_list
    #     List of pandas dataframe objects
    #
    # relationship_dict
    #     This is an existing relationship_dict.  If None, a new
    #     relationship_dict should be created

    # adds relationship_dict if there isn't one
    for table in dataframe_list:
       if table not in relationship_dict:
           relationship_dict[table] = {}

       print('table: ', end='')
       print(table)
       for col in dataframe_list[table].columns:
           if col not in relationship_dict[table]:
               relationship_dict[table][col] = {}
           print('  col: ', end='')
           print(col, end=': ')
           # primary key candidate must have unique values
           total = dataframe_list[table][col].count()
           unique = dataframe_list[table][col].nunique()
           print(total, end=': ')
           print(unique)
           if total == unique:
               relationship_dict[table][col]['key_candidate'] = True
               print('found a primary key candidate')
           else:
               relationship_dict[table][col]['key_candidate'] = False

    ###
    # Student code (create additional functions as necessary)
    ###

    # mock-up for demonstration - remove after development
    # relationship_dict['airlines']['carrier']['key_candidate'] = True
    # relationship_dict['airports']['dest']['key_candidate'] = True
    # relationship_dict['flights']['dest']['key_candidate'] = False
    # relationship_dict['flights']['carrier']['key_candidate'] = False
    # relationship_dict['flights']['flight_id']['key_candidate'] = True
    # relationship_dict['trip_logs']['flight_id']['key_candidate'] = False

    # return relationship structure
    return relationship_dict

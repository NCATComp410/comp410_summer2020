import pandas as pd
import os
import git



def pecan_cookies_load_data():
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    pd.set_option('display.width', 15000)

    data = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'data')

    airports = pd.read_csv(os.path.join(data, 'airports', 'airports.csv'))
    airlines = pd.read_csv(os.path.join(data, 'airlines', 'airlines.csv'))
    flights = pd.read_csv(os.path.join(data, 'flights', 'flights.csv'))

    dataframe_list = {
        'airports': airports,
        'airlines': airlines,
        'flights': flights
    }

    return dataframe_list


def find_similar_data(current_table, current_col, dataframe_dict):
    relationship_list = []

    target_set = set(dataframe_dict[current_table][current_col])
    for table in dataframe_dict:
        if table != current_table:
            for col in dataframe_dict[table]:
                compare_set = set(dataframe_dict[table][col])
                if target_set.issubset(compare_set) or target_set.issuperset(compare_set):
                    relationship_list.append({table + '.' + col: {}})

    return relationship_list

  
def search_by_name(df_list, rel_dict):
    # start by iterating through the table and columns once
    for table in df_list:
        print('+' + table)
        for col in df_list[table].columns:

            # after getting to the first column, we need to start working through the data again
            # table by table

            for tbl in df_list:

                # given that that the tables are not the same table, we can move forward.

                if tbl != table:
                    print('-' + tbl)
                    # delineation is made to show we are working within different parts of the
                    # data to ensure no overlap is done between identical tables.

                    for cln in df_list[tbl].columns:

                        # additionally, we should compare column results to ensure we are finding a relationship
                        # This relationship is present if the column names of different tables are identical

                        if cln == col:

                            # Finally, it should be determined if the relationship has been found in the
                            # relationship dictionary. If that relationship doesn't exist, we simply add it

                            # we should check by table value first and instantiate if it doesn't exist in the
                            # the rel_dict
                            if tbl not in rel_dict:
                                rel_dict[tbl] = {}

                            # after checking the table existance in rel_dict, we should check for the column
                            # and add it as necessary
                            if cln not in rel_dict[tbl]:
                                rel_dict[tbl][cln] = {'relationships': []}

                            # make sure the relationships index exists
                            if 'relationships' not in rel_dict[tbl][cln]:
                                rel_dict[tbl][cln]['relationships'] = []

                            # finally adding the relationship to the rel_dict
                            relationship = '.'.join([table, cln])
                            rel_dict[tbl][cln]['relationships'].append({relationship: {}})

                            print(' ' + col)
                            # We print the column only when it exists in a relationship that should be added.


def find_related_cols_by_name(dataframe_list, relationship_dict=None):
    # dataframe_list
    #     List of pandas dataframe objects
    #
    # relationship_dict
    #     This is an existing relationship_dict.  If None, a new
    #     relationship_dict should be created

    ###
    # Student code (create additional functions as necessary)
    ###

    # print the tables as they are represented

    for table in dataframe_list:
        print(table)
        for col in dataframe_list[table].columns:
            print(' ' + col)

    if relationship_dict is None:
        relationship_dict = {}

    search_by_name(dataframe_list, relationship_dict)
    # print('relationship dictionary for sbn: ')

    # mock-up for demonstration - remove after development
    # relationship_dict['airlines']['carrier']['relationships'] = [{'flights.carrier': {}}]
    # relationship_dict['airports']['dest']['relationships'] = [{'flights.dest': {}}]
    # relationship_dict['flights']['dest']['relationships'] = [{'airports.dest': {}}]
    # relationship_dict['flights']['carrier']['relationships'] = [{'airlines.carrier': {}}]
    # relationship_dict['flights']['flight_id']['relationships'] = [{'trip_logs.flight_id': {}}]
    # relationship_dict['trip_logs']['flight_id']['relationships'] = [{'flights.flight_id': {}}]

    # return relationship structure
    return relationship_dict


def find_related_cols_by_content(dataframe_list, relationship_dict=None):
    # if the data list is empty return None
    if dataframe_list is None:
        return relationship_dict

    # if the relationship dictionary is None create an empty relationship dictionary
    if relationship_dict is None:
        relationship_dict = {}

    for table in dataframe_list:
        # create a short-hand reference to the actual dataframe
        df = dataframe_list[table]

        # If this table is not in the relationship_dict, add it
        if table not in relationship_dict:
            relationship_dict[table] = {}

        # If a column is not in the relationship dict, add it
        for col in df.columns:
            if col not in relationship_dict[table]:
                relationship_dict[table][col] = {'key_candidate': 'False',
                                                 'relationships': find_similar_data(table, col, dataframe_list)}

    return relationship_dict


def find_parent_child_relationships(dataframe_list, relationship_dict, hints=None):
    # dataframe_list
    #     List of pandas dataframe objects
    #
    # relationship_dict
    #     And existing relationship_dict is required
    #
    # hints
    #     Structure containing hints in cases where the data is ambiguous such
    #     as when two columns are related and appear to be primary key candidates
    #     in both tables. Format is:
    #         [{parent table.column: child table.column}, ...]

    ###
    # Student code (create additional functions as necessary)
    ###

    for table in relationship_dict:
        print(table)
        for col in relationship_dict[table]:
            print(col)
            if relationship_dict[table][col]['key_candidate'] is True:
                print('Found a primary key candidate')
                for relationship in relationship_dict[table][col]['relationships']:
                    for table_column_name in relationship:
                        relationship[table_column_name]['type'] = 'Parent'
            else:
                for relationship in relationship_dict[table][col]['relationships']:
                    for table_column_name in relationship:
                        relationship[table_column_name]['type'] = 'Child'

    # # mock-up for demonstration - remove after development
    # relationship_dict['airlines']['carrier']['relationships'] = [{'flights.carrier': {'type': 'Parent'}}]
    # relationship_dict['airports']['dest']['relationships'] = [{'flights.dest': {'type': 'Parent'}}]
    # relationship_dict['flights']['dest']['relationships'] = [{'airports.dest': {'type': 'Child'}}]
    # relationship_dict['flights']['carrier']['relationships'] = [{'airlines.carrier': {'type': 'Child'}}]
    # relationship_dict['flights']['flight_id']['relationships'] = [{'trip_logs.flight_id': {'type': 'Parent'}}]
    # relationship_dict['trip_logs']['flight_id']['relationships'] = [{'flights.flight_id': {'type': 'Child'}}]

    # return relationship structure
    return relationship_dict

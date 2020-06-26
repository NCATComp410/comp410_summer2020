import pandas as pd


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
                            if cln not in rel_dict:
                                rel_dict[tbl][cln] = { 'relationships': []}

                            # finally adding the relationship to the rel_dict
                            rel_dict[tbl][cln]['relationships'].append({table: cln})
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
    # dataframe_list
    #     List of pandas dataframe objects
    #
    # relationship_dict
    #     This is an existing relationship_dict.  If None, a new
    #     relationship_dict should be created


    ###
    # Student code (create additional functions as necessary)
    ###

    # return relationship structure
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

    # mock-up for demonstration - remove after development
    relationship_dict['airlines']['carrier']['relationships'] = [{'flights.carrier': {'type': 'Parent'}}]
    relationship_dict['airports']['dest']['relationships'] = [{'flights.dest': {'type': 'Parent'}}]
    relationship_dict['flights']['dest']['relationships'] = [{'airports.dest': {'type': 'Child'}}]
    relationship_dict['flights']['carrier']['relationships'] = [{'airlines.carrier': {'type': 'Child'}}]
    relationship_dict['flights']['flight_id']['relationships'] = [{'trip_logs.flight_id': {'type': 'Parent'}}]
    relationship_dict['trip_logs']['flight_id']['relationships'] = [{'flights.flight_id': {'type': 'Child'}}]

    # return relationship structure
    return relationship_dict

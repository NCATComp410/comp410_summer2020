import pandas as pd

def find_similar_data(current_table, current_col, dataframe_dict):

    # Will return empty list if no relationships found
    relationship_list = []

    # create a target set which will be used for comparisons
    target_set = set(dataframe_dict[current_table][current_col])
    for table in dataframe_dict:
        if table != current_table:
            for col in dataframe_dict[table].columns:
                compare_set = set(dataframe_dict[table][col])
                if target_set.issubset(compare_set) or target_set.issuperset(compare_set):
                    relationship_list.append({table + '.' + col: {}})

    return relationship_list


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

    # mock-up for demonstration - remove after development
    relationship_dict['airlines']['carrier']['relationships'] = [{'flights.carrier': {}}]
    relationship_dict['airports']['dest']['relationships'] = [{'flights.dest': {}}]
    relationship_dict['flights']['dest']['relationships'] = [{'airports.dest': {}}]
    relationship_dict['flights']['carrier']['relationships'] = [{'airlines.carrier': {}}]
    relationship_dict['flights']['flight_id']['relationships'] = [{'trip_logs.flight_id': {}}]
    relationship_dict['trip_logs']['flight_id']['relationships'] = [{'flights.flight_id': {}}]

    # return relationship structure
    return relationship_dict


def find_related_cols_by_content(dataframe_dict, relationship_dict=None):
    # dataframe_list
    #     List of pandas dataframe objects
    #
    # relationship_dict
    #     This is an existing relationship_dict.  If None, a new
    #     relationship_dict should be created

    if relationship_dict==None:
        relationship_dict = {}
    
    for table_name in dataframe_dict:
        # Adding table if it doesn't exist
        if table_name not in relationship_dict:
            relationship_dict[table_name] = {}

        for col_name in dataframe_dict[table_name]:
            # Adding column if it doesn't exist
            if col_name not in relationship_dict[table_name]:
                relationship_dict[table_name][col_name] = {}
            
            # Getting relationship
            # NOTE: it replaces any existing relationship. bug or feature?
            relationship_dict[table_name][col_name]['relationship'] = find_similar_data(table_name,col_name,dataframe_dict)

    print(relationship_dict)

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

import pandas as pd


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

import unittest
import pandas as pd
import git
import os
from dfstools import get_dataset_dtypes
from dfstools import find_related_cols_by_name
from dfstools import find_related_cols_by_content
from dfstools import find_parent_child_relationships
from dfstools import pecan_cookies_load_data


class DataTools(unittest.TestCase):

    def test_get_dataset_dtypes(self):

        '''
        expected = {'airlines': {'carrier': {'dtype': 'O'}},
                    'airports': {'dest': {'dtype': 'O'}},
                    'flights': {'dest': {'dtype': 'O'}, 'carrier': {'dtype': 'O'},'flight_id': {'dtype': 'O'}},
                    'trip_logs': {'flight_id': {'dtype': 'O'}}}
        result = get_dataset_dtypes(None)
        self.assertEqual(expected, result)

        expected = {
                    'airlines': {'carrier': {'dtype': 'O',
                                             # 'key_candidate': True,
                                             'relationships': [{'flights.carrier': {}}]}},
                    'airports': {'dest': {'dtype': 'O',
                                          # 'key_candidate': True,
                                          'relationships': [{'flights.dest': {}}]}},
                    'flights': {'dest': {'dtype': 'O',
                                         # 'key_candidate': False,
                                         'relationships': [{'airports.dest': {}}]},
                                'carrier': {'dtype': 'O',
                                            # 'key_candidate': False,
                                            'relationships': [{'airlines.carrier': {}}]},
                                'flight_id': {'dtype': 'O',
                                              # 'key_candidate': True,
                                              'relationships': [{'trip_logs.flight_id': {}}]}},
                    'trip_logs': {'flight_id': {'dtype': 'O',
                                                # 'key_candidate': False,
                                                'relationships': [{'flights.flight_id': {}}]}}}

        data = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'data')

        dataframe_dict = {'airlines': pd.read_csv(os.path.join(data, 'airlines', 'airlines.csv')),
                          'flights': pd.read_csv(os.path.join(data, 'flights', 'flights.csv')),
                          'airports': pd.read_csv(os.path.join(data, 'airports', 'airports.csv'))}

        result = find_related_cols_by_name(dataframe_dict, result)
        self.assertEqual(expected, result)
        '''

        # ---pecan cookies sprint one test case---

        expected = {
                    'airports': {'dest': {'relationships': ['flights.origin', 'flights.dest']},
                                 'dest_city': {'relationships': ['flights.origin_city']},
                                 'dest_state': {'relationships': ['flights.origin_state']}},

                    'airlines': {'carrier': {'relationships': ['flights.carrier']}},

                    "flights": {
                        "flight_id": {"relationships": []},
                        "origin": {"relationships": ["airports.dest"]},
                        "origin_city": {"relationships": ["airports.dest_city"]},
                        "origin_state": {"relationships": ["airports.dest_state"]},
                        "dest": {"relationships": ["airports.dest"]},
                        "distance_group": {"relationships": []},
                        "carrier": {"relationships": ["airlines.carrier"]},
                        "flight_num": {"relationships": []},
                        "first_trip_logs_time": {"relationships": []}}
                    }
        data_list = pecan_cookies_load_data()
        result = find_related_cols_by_content(data_list)
        self.assertEqual(expected, result)


        #result = find_parent_child_relationships(None, result)
        #self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

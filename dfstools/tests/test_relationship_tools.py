import unittest
import pandas as pd
from dfstools import get_dataset_dtypes
from dfstools import find_related_cols_by_name
from dfstools import find_related_cols_by_content
from dfstools import find_parent_child_relationships


class DataTools(unittest.TestCase):
    def test_get_dataset_dtypes(self):
        expected = {'airlines': {'carrier': {'dtype': 'O'}},
                    'airports': {'dest': {'dtype': 'O'}},
                    'flights': {'dest': {'dtype': 'O'}, 'carrier': {'dtype': 'O'},'flight_id': {'dtype': 'O'}},
                    'trip_logs': {'flight_id': {'dtype': 'O'}}}
        result = get_dataset_dtypes(None)
        self.assertEqual(expected, result)

        expected = {'airlines': {'carrier': {'dtype': 'O',
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

        dataframe_dict = {'airlines': pd.read_csv('../data/airlines/airlines.csv'),
                          'flights': pd.read_csv('../data/flights/flights.csv'),
                          'airports': pd.read_csv('../data/airports/airports.csv')}

        result = find_related_cols_by_name(dataframe_dict, result)
        self.assertEqual(expected, result)

        result = find_related_cols_by_content(None, result)
        self.assertEqual(expected, result)

        expected = {'airlines': {'carrier': {'dtype': 'O',
                                             # 'key_candidate': True,
                                             'relationships': [{'flights.carrier': {'type': 'Parent'}}]}},
                    'airports': {'dest': {'dtype': 'O',
                                          # 'key_candidate': True,
                                          'relationships': [{'flights.dest': {'type': 'Parent'}}]}},
                    'flights': {'dest': {'dtype': 'O',
                                         # 'key_candidate': False,
                                         'relationships': [{'airports.dest': {'type': 'Child'}}]},
                                'carrier': {'dtype': 'O',
                                            # 'key_candidate': False,
                                            'relationships': [{'airlines.carrier': {'type': 'Child'}}]},
                                'flight_id': {'dtype': 'O',
                                              # 'key_candidate': True,
                                              'relationships': [{'trip_logs.flight_id': {'type': 'Parent'}}]}},
                    'trip_logs': {'flight_id': {'dtype': 'O',
                                                # 'key_candidate': False,
                                                'relationships': [{'flights.flight_id': {'type': 'Child'}}]}}}
        result = find_parent_child_relationships(None, result)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

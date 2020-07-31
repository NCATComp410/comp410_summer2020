import unittest
import pandas as pd
import git
import os
from dfstools import get_dataset_dtypes
from dfstools import find_primary_key_candidates


class DataTools(unittest.TestCase):
    def test_find_primary_key_candidates(self):

        # Get initial relationships_dict
        expected = {'airlines': {'carrier': {'dtype': 'object'}},
                    'airports': {'dest': {'dtype': 'object'},
                                 'dest_city': {'dtype': 'object'},
                                 'dest_state': {'dtype': 'object'}},
                    'flights': {'carrier': {'dtype': 'object'},
                                'dest': {'dtype': 'object'},
                                'distance_group': {'dtype': 'int64'},
                                'first_trip_logs_time': {'dtype': 'object'},
                                'flight_id': {'dtype': 'object'},
                                'flight_num': {'dtype': 'int64'},
                                'origin': {'dtype': 'object'},
                                'origin_city': {'dtype': 'object'},
                                'origin_state': {'dtype': 'object'}},
                    'trip_logs': {'air_time': {'dtype': 'float64'},
                                  'arr_delay': {'dtype': 'float64'},
                                  'arr_time': {'dtype': 'object'},
                                  'canceled': {'dtype': 'float64'},
                                  'carrier_delay': {'dtype': 'float64'},
                                  'date_scheduled': {'dtype': 'object'},
                                  'dep_delay': {'dtype': 'float64'},
                                  'dep_time': {'dtype': 'object'},
                                  'distance': {'dtype': 'float64'},
                                  'diverted': {'dtype': 'float64'},
                                  'flight_id': {'dtype': 'object'},
                                  'late_aircraft_delay': {'dtype': 'float64'},
                                  'national_airspace_delay': {'dtype': 'float64'},
                                  'scheduled_arr_time': {'dtype': 'object'},
                                  'scheduled_dep_time': {'dtype': 'object'},
                                  'scheduled_elapsed_time': {'dtype': 'int64'},
                                  'security_delay': {'dtype': 'float64'},
                                  'taxi_in': {'dtype': 'float64'},
                                  'taxi_out': {'dtype': 'float64'},
                                  'trip_log_id': {'dtype': 'int64'},
                                  'weather_delay': {'dtype': 'float64'}}}

        data = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'data')

        dataframe_dict = {'airlines': pd.read_csv(os.path.join(data, 'airlines', 'airlines.csv')),
                          'flights': pd.read_csv(os.path.join(data, 'flights', 'flights.csv')),
                          'airports': pd.read_csv(os.path.join(data, 'airports', 'airports.csv')),
                          'trip_logs': pd.read_csv(os.path.join(data, 'trip_logs', 'trip_logs.csv'))}

        result = get_dataset_dtypes(dataframe_dict)
        self.assertEqual(expected, result)

        expected = {'airlines': {'carrier': {'dtype': 'object', 'key_candidate': True}},
                    'airports': {'dest': {'dtype': 'object', 'key_candidate': True},
                                 'dest_city': {'dtype': 'object', 'key_candidate': False},
                                 'dest_state': {'dtype': 'object', 'key_candidate': False}},
                    'flights': {'carrier': {'dtype': 'object', 'key_candidate': False},
                                'dest': {'dtype': 'object', 'key_candidate': False},
                                'distance_group': {'dtype': 'int64', 'key_candidate': False},
                                'first_trip_logs_time': {'dtype': 'object',
                                                         'key_candidate': False},
                                'flight_id': {'dtype': 'object', 'key_candidate': True},
                                'flight_num': {'dtype': 'int64', 'key_candidate': False},
                                'origin': {'dtype': 'object', 'key_candidate': False},
                                'origin_city': {'dtype': 'object', 'key_candidate': False},
                                'origin_state': {'dtype': 'object', 'key_candidate': False}},
                    'trip_logs': {'air_time': {'dtype': 'float64', 'key_candidate': False},
                                  'arr_delay': {'dtype': 'float64', 'key_candidate': False},
                                  'arr_time': {'dtype': 'object', 'key_candidate': False},
                                  'canceled': {'dtype': 'float64', 'key_candidate': False},
                                  'carrier_delay': {'dtype': 'float64', 'key_candidate': False},
                                  'date_scheduled': {'dtype': 'object', 'key_candidate': False},
                                  'dep_delay': {'dtype': 'float64', 'key_candidate': False},
                                  'dep_time': {'dtype': 'object', 'key_candidate': False},
                                  'distance': {'dtype': 'float64', 'key_candidate': False},
                                  'diverted': {'dtype': 'float64', 'key_candidate': False},
                                  'flight_id': {'dtype': 'object', 'key_candidate': False},
                                  'late_aircraft_delay': {'dtype': 'float64',
                                                          'key_candidate': False},
                                  'national_airspace_delay': {'dtype': 'float64',
                                                              'key_candidate': False},
                                  'scheduled_arr_time': {'dtype': 'object',
                                                         'key_candidate': False},
                                  'scheduled_dep_time': {'dtype': 'object',
                                                         'key_candidate': False},
                                  'scheduled_elapsed_time': {'dtype': 'int64',
                                                             'key_candidate': False},
                                  'security_delay': {'dtype': 'float64', 'key_candidate': False},
                                  'taxi_in': {'dtype': 'float64', 'key_candidate': False},
                                  'taxi_out': {'dtype': 'float64', 'key_candidate': False},
                                  'trip_log_id': {'dtype': 'int64', 'key_candidate': True},
                                  'weather_delay': {'dtype': 'float64', 'key_candidate': False}}}

        result = find_primary_key_candidates(dataframe_dict, result)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

import unittest
import pandas as pd
import git
import os
from dfstools import get_dataset_dtypes
from dfstools import find_primary_key_candidates


class DataTools(unittest.TestCase):
    def test_find_primary_key_candidates(self):

        # Get initial relationships_dict
        expected = {'airlines': {'carrier': {'dtype': 'O'}},
                    'airports': {'dest': {'dtype': 'O'}},
                    'flights': {'dest': {'dtype': 'O'}, 'carrier': {'dtype': 'O'},'flight_id': {'dtype': 'O'}},
                    'trip_logs': {'flight_id': {'dtype': 'O'}}}
        result = get_dataset_dtypes(None)
        self.assertEqual(expected, result)

        data = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'data')

        dataframe_dict = {'airlines': pd.read_csv(os.path.join(data, 'airlines', 'airlines.csv')),
                          'flights': pd.read_csv(os.path.join(data, 'flights', 'flights.csv')),
                          'airports': pd.read_csv(os.path.join(data, 'airports', 'airports.csv')),
                          'trip_logs': pd.read_csv(os.path.join(data, 'trip_logs', 'trip_logs.csv'))}

        expected = {'airlines': {'carrier': {'dtype': 'O', 'key_candidate': True}},
                    'airports': {'dest': {'dtype': 'O', 'key_candidate': True},
                                 'dest_city': {'key_candidate': False},
                                 'dest_state': {'key_candidate': False}},
                    'flights': {'carrier': {'dtype': 'O', 'key_candidate': False},
                                'dest': {'dtype': 'O', 'key_candidate': False},
                                'distance_group': {'key_candidate': False},
                                'first_trip_logs_time': {'key_candidate': False},
                                'flight_id': {'dtype': 'O', 'key_candidate': True},
                                'flight_num': {'key_candidate': False},
                                'origin': {'key_candidate': False},
                                'origin_city': {'key_candidate': False},
                                'origin_state': {'key_candidate': False}},
                    'trip_logs': {'air_time': {'key_candidate': False},
                                  'arr_delay': {'key_candidate': False},
                                  'arr_time': {'key_candidate': False},
                                  'canceled': {'key_candidate': False},
                                  'carrier_delay': {'key_candidate': False},
                                  'date_scheduled': {'key_candidate': False},
                                  'dep_delay': {'key_candidate': False},
                                  'dep_time': {'key_candidate': False},
                                  'distance': {'key_candidate': False},
                                  'diverted': {'key_candidate': False},
                                  'flight_id': {'dtype': 'O', 'key_candidate': False},
                                  'late_aircraft_delay': {'key_candidate': False},
                                  'national_airspace_delay': {'key_candidate': False},
                                  'scheduled_arr_time': {'key_candidate': False},
                                  'scheduled_dep_time': {'key_candidate': False},
                                  'scheduled_elapsed_time': {'key_candidate': False},
                                  'security_delay': {'key_candidate': False},
                                  'taxi_in': {'key_candidate': False},
                                  'taxi_out': {'key_candidate': False},
                                  'trip_log_id': {'key_candidate': True},
                                  'weather_delay': {'key_candidate': False}}}
        result = find_primary_key_candidates(dataframe_dict, result)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

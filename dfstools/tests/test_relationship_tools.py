import unittest
import pandas as pd
import git
import os
from dfstools import get_dataset_dtypes
from dfstools import find_related_cols_by_name
from dfstools import find_related_cols_by_content
from dfstools import find_parent_child_relationships


class RelationshipTools(unittest.TestCase):
    def test_get_dataset_dtypes(self):
        expected = {'airlines': {'carrier': {'dtype': 'O'}},
                    'airports': {'dest': {'dtype': 'O'}},
                    'flights': {'dest': {'dtype': 'O'}, 'carrier': {'dtype': 'O'},'flight_id': {'dtype': 'O'}},
                    'trip_logs': {'flight_id': {'dtype': 'O'}}}
        result = get_dataset_dtypes(None)
        self.assertEqual(expected, result)

    def test_find_related_cols_by_name(self):
        result = get_dataset_dtypes(None)
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
                          'airports': pd.read_csv(os.path.join(data, 'airports', 'airports.csv')),
                          'trip_logs': pd.read_csv(os.path.join(data, 'trip_logs', 'trip_logs.csv'))}

        result = find_related_cols_by_name(dataframe_dict, result)
        self.assertEqual(expected, result)

    def test_find_related_cols_by_content(self):
        # ---pecan cookies sprint one test case---

        # expected = {'airlines': {'carrier': {'key_candidate': 'False',
        #                                      'relationships': [{'flights.carrier': {}}]}},
        #             'airports': {'dest': {'key_candidate': 'False',
        #                                   'relationships': [{'flights.origin': {}},
        #                                                     {'flights.dest': {}}]},
        #                          'dest_city': {'key_candidate': 'False',
        #                                        'relationships': [{'flights.origin_city': {}}]},
        #                          'dest_state': {'key_candidate': 'False',
        #                                         'relationships': [{'flights.origin_state': {}}]}},
        #             'flights': {'carrier': {'key_candidate': 'False',
        #                                     'relationships': [{'airlines.carrier': {}}]},
        #                         'dest': {'key_candidate': 'False',
        #                                  'relationships': [{'airports.dest': {}}]},
        #                         'distance_group': {'key_candidate': 'False', 'relationships': []},
        #                         'first_trip_logs_time': {'key_candidate': 'False',
        #                                                  'relationships': []},
        #                         'flight_id': {'key_candidate': 'False', 'relationships': []},
        #                         'flight_num': {'key_candidate': 'False', 'relationships': []},
        #                         'origin': {'key_candidate': 'False',
        #                                    'relationships': [{'airports.dest': {}}]},
        #                         'origin_city': {'key_candidate': 'False',
        #                                         'relationships': [{'airports.dest_city': {}}]},
        #                         'origin_state': {'key_candidate': 'False',
        #                                          'relationships': [{'airports.dest_state': {}}]}}}

        expected = {'airlines': {'carrier': {'key_candidate': 'False',
                                             'relationships': [{'flights.carrier': {}}]}},
                    'airports': {'dest': {'key_candidate': 'False',
                                          'relationships': [{'flights.origin': {}},
                                                            {'flights.dest': {}}]},
                                 'dest_city': {'key_candidate': 'False',
                                               'relationships': [{'flights.origin_city': {}}]},
                                 'dest_state': {'key_candidate': 'False',
                                                'relationships': [{'flights.origin_state': {}}]}},
                    'flights': {'carrier': {'key_candidate': 'False',
                                            'relationships': [{'airlines.carrier': {}}]},
                                'dest': {'key_candidate': 'False',
                                         'relationships': [{'airports.dest': {}}]},
                                'distance_group': {'key_candidate': 'False',
                                                   'relationships': [{'trip_logs.trip_log_id': {}},
                                                                     {'trip_logs.dep_delay': {}},
                                                                     {'trip_logs.taxi_out': {}},
                                                                     {'trip_logs.taxi_in': {}},
                                                                     {'trip_logs.arr_delay': {}},
                                                                     {'trip_logs.carrier_delay': {}},
                                                                     {'trip_logs.weather_delay': {}},
                                                                     {'trip_logs.national_airspace_delay': {}},
                                                                     {'trip_logs.security_delay': {}},
                                                                     {'trip_logs.late_aircraft_delay': {}}]},
                                'first_trip_logs_time': {'key_candidate': 'False',
                                                         'relationships': []},
                                'flight_id': {'key_candidate': 'False',
                                              'relationships': [{'trip_logs.flight_id': {}}]},
                                'flight_num': {'key_candidate': 'False',
                                               'relationships': [{'trip_logs.trip_log_id': {}}]},
                                'origin': {'key_candidate': 'False',
                                           'relationships': [{'airports.dest': {}}]},
                                'origin_city': {'key_candidate': 'False',
                                                'relationships': [{'airports.dest_city': {}}]},
                                'origin_state': {'key_candidate': 'False',
                                                 'relationships': [{'airports.dest_state': {}}]}},
                    'trip_logs': {'air_time': {'key_candidate': 'False', 'relationships': []},
                                  'arr_delay': {'key_candidate': 'False',
                                                'relationships': [{'flights.distance_group': {}}]},
                                  'arr_time': {'key_candidate': 'False', 'relationships': []},
                                  'canceled': {'key_candidate': 'False', 'relationships': []},
                                  'carrier_delay': {'key_candidate': 'False',
                                                    'relationships': [{'flights.distance_group': {}}]},
                                  'date_scheduled': {'key_candidate': 'False',
                                                     'relationships': []},
                                  'dep_delay': {'key_candidate': 'False',
                                                'relationships': [{'flights.distance_group': {}}]},
                                  'dep_time': {'key_candidate': 'False', 'relationships': []},
                                  'distance': {'key_candidate': 'False', 'relationships': []},
                                  'diverted': {'key_candidate': 'False', 'relationships': []},
                                  'flight_id': {'key_candidate': 'False',
                                                'relationships': [{'flights.flight_id': {}}]},
                                  'late_aircraft_delay': {'key_candidate': 'False',
                                                          'relationships': [{'flights.distance_group': {}}]},
                                  'national_airspace_delay': {'key_candidate': 'False',
                                                              'relationships': [{'flights.distance_group': {}}]},
                                  'scheduled_arr_time': {'key_candidate': 'False',
                                                         'relationships': []},
                                  'scheduled_dep_time': {'key_candidate': 'False',
                                                         'relationships': []},
                                  'scheduled_elapsed_time': {'key_candidate': 'False',
                                                             'relationships': []},
                                  'security_delay': {'key_candidate': 'False',
                                                     'relationships': [{'flights.distance_group': {}}]},
                                  'taxi_in': {'key_candidate': 'False',
                                              'relationships': [{'flights.distance_group': {}}]},
                                  'taxi_out': {'key_candidate': 'False',
                                               'relationships': [{'flights.distance_group': {}}]},
                                  'trip_log_id': {'key_candidate': 'False',
                                                  'relationships': [{'flights.distance_group': {}},
                                                                    {'flights.flight_num': {}}]},
                                  'weather_delay': {'key_candidate': 'False',
                                                    'relationships': [{'flights.distance_group': {}}]}}}

        # data_list = pecan_cookies_load_data()

        data = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'data')

        data_list = {'airlines': pd.read_csv(os.path.join(data, 'airlines', 'airlines.csv')),
                          'flights': pd.read_csv(os.path.join(data, 'flights', 'flights.csv')),
                          'airports': pd.read_csv(os.path.join(data, 'airports', 'airports.csv')),
                          'trip_logs': pd.read_csv(os.path.join(data, 'trip_logs', 'trip_logs.csv'))}

        result = find_related_cols_by_content(data_list)
        self.assertEqual(expected, result)


        #result = find_parent_child_relationships(None, result)
        #self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

import unittest
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

        expected = {'airlines': {'carrier': {'dtype': 'O', 'key_candidate': True}},
                    'airports': {'dest': {'dtype': 'O', 'key_candidate': True}},
                    'flights': {'dest': {'dtype': 'O', 'key_candidate': False},
                                'carrier': {'dtype': 'O', 'key_candidate': False},
                                'flight_id': {'dtype': 'O', 'key_candidate': True}},
                    'trip_logs': {'flight_id': {'dtype': 'O', 'key_candidate': False}}}
        result = find_primary_key_candidates(None, result)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

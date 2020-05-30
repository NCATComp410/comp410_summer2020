import unittest
from dfstools import load_csv_to_df


class CsvTools(unittest.TestCase):
    def test_load_csv_to_df(self):
        expected = ['airlines', 'airports', 'flights', 'trip_logs']
        result = load_csv_to_df(None)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

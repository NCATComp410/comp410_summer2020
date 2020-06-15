import unittest
import pytest
from dfstools import show_aggie_pride
from dfstools import load_csv_to_df


class CsvTools(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_show_aggie_pride(self):
        show_aggie_pride()

        # read the capture buffer so far
        out, err = self.capsys.readouterr()

        # make sure the message was actually printed 
        self.assertEqual('Aggie Pride - World wide\n', out)


    def test_load_csv_to_df(self):
        expected = ['airlines', 'airports', 'flights', 'trip_logs']
        result = load_csv_to_df(None)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

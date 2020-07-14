import unittest
import pytest
import git
import os
from dfstools import show_aggie_pride
from dfstools import load_csv_to_df
from dfstools import find_csv_files


class CsvTools(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_show_aggie_pride(self):
        show_aggie_pride()

        # read the capture buffer so far
        out, err = self.capsys.readouterr()

        # make sure the message was actually printed 
        self.assertEqual('Aggie Pride - Worldwide\n', out)

    def test_find_csv_files_include_hidden(self):
        # This will test to make sure include_hidden parameter works as expected
        # Find the data directory for this repo
        data_path = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'data')

        # Test the case where include_hidden==False
        # List of filenames we expect to see.  Order is not important
        # Full path is not important
        expected = {'flights.csv',
                    'invalid_logs.csv',
                    'trip_logs.csv',
                    'airlines.csv',
                    'airports.csv'}

        result = find_csv_files(data_path,
                                include_hidden=False,
                                traverse_subdir=True,
                                follow_symlink=False)

        # Make sure all expected file names are present
        for e in expected:
            self.assertIn(e, next((s for s in result if e in s), result))

        # .old_trip_logs.csv should not be present since it is a hidden file
        self.assertNotIn('.old_trip_logs.csv', result)

        # Now test the true case
        result = find_csv_files(data_path,
                                include_hidden=True,
                                traverse_subdir=True,
                                follow_symlink=False)

        # Make sure all expected file names are present
        for e in expected:
            self.assertIn(e, next((s for s in result if e in s), result))

        # .old_trip_logs.csv should now be present
        self.assertIn('.old_trip_logs.csv', result)

    def test_load_csv_to_df(self):
        expected = {'airlines', 'airports', 'flights', 'trip_logs'}

        data_path = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'data')

        dataframe_dict = load_csv_to_df(data_path,
                                        include_hidden=False,
                                        traverse_subdir=True,
                                        ignore_errors=True,
                                        follow_symlink=False)

        self.assertEqual(expected, set(dataframe_dict.keys()))


if __name__ == '__main__':
    unittest.main()

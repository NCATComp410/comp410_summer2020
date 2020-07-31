import unittest
import pytest
import git
import os
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
        self.assertEqual('Aggie Pride - Worldwide\n', out)

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

import unittest
import pytest


class ConsoleTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_print_message(self):
        # print a message
        print('test message')

        # read the capture buffer so far
        out, err = self.capsys.readouterr()

        # make sure the message was actually printed 
        self.assertEqual('test message\n', out)


if __name__ == '__main__':
    unittest.main()

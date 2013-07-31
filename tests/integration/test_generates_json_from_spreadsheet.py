import json
import shlex
import subprocess
import tempfile
import unittest
from hamcrest import *
from mock import patch
from collector.spreadsheet_to_json import spreadsheet_to_json


class TestJsonGeneratedFromSpreadsheet(unittest.TestCase):

    def setUp(self):
        self.data = [['foo', 'bar', 'zap'],[1,2,3],[4,5,6]]
        self.config = {
            "doc_name": {
                "username": "_",
                "password": "_",
                "key": "_"
            }
        }

    @patch("collector.spreadsheet_to_json.get_google_spreadsheet_data")
    @patch("sys.stdout.write")
    def test_something(self, mock_stdout, mock_spreadsheet_data):
        f = tempfile.NamedTemporaryFile(suffix=".json")
        f.write(json.dumps(self.config))
        f.flush()

        mock_spreadsheet_data.return_value = self.data

        spreadsheet_to_json(("--doc doc_name --config %s" % f.name).split())

        mock_stdout.assert_called_with('[{"foo": 1, "bar": 2, "zap": 3}, '
                                       '{"foo": 4, "bar": 5, "zap": 6}]')




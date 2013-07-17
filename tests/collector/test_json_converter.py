import unittest
from hamcrest import *
from collector.json_converter import JsonConverter

class TestJsonConverter(unittest.TestCase):

    def test_it_converts_list_of_lists_into_json(self):
        converter = JsonConverter()
        data = [
            ['Column1', 'Column2', 'Column3'],
            ['Value11', 'Value12', 'Value13'],
            ['Value21', 'Value22', 'Value23'],
            ['Value31', 'Value32', 'Value33']
        ]
        expected_json = [
            { 'Column1': 'Value11', 'Column2': 'Value12', 'Column3': 'Value13'},
            { 'Column1': 'Value21', 'Column2': 'Value22', 'Column3': 'Value23'},
            { 'Column1': 'Value31', 'Column2': 'Value32', 'Column3': 'Value33'}
        ]
        
        assert_that(converter.convert(data), is_(expected_json))

import sys
import gspread
import argparse
import json

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help="Google Spreadsheet username",
                        required=True)
    parser.add_argument('--password', help="Google Spreadsheet password. Can be a application specific password",
                        required=True)
    parser.add_argument('--key', help="Google Spreadsheet's key, from the URL",
                        required=True)

    return parser.parse_args(args)
    
def to_dict(data):
    header, rows = data[0], data[1:]

    def maybe_convert_to_number(s):
        try:
            return int(s)
        except (ValueError, TypeError):
            return s

    def row_to_dict(row):
        converted_row = map(maybe_convert_to_number, row)
        return dict(zip(header, converted_row))

    return map(row_to_dict, rows)      


def spreadsheet_to_json(args):
    arguments = parse_args(args)

    gs = gspread.login(arguments.username, arguments.password)
    sh = gs.open_by_key(arguments.key)
    
    data = sh.sheet1.get_all_values()
    
    print json.dumps(to_dict(data))

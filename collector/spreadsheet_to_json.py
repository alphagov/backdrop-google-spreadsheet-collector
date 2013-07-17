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

def get_google_spreadsheet_data(username, password, key):
    google = gspread.login(username, password)
    spreadsheet = google.open_by_key(key)
    
    return spreadsheet.sheet1.get_all_values()
    
def convert_to_records(data):
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
    raw_data = get_google_spreadsheet_data(arguments.username,
                                           arguments.password,
                                           arguments.key)

    print json.dumps(convert_to_records(raw_data))

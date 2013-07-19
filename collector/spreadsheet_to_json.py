import sys
import gspread
import argparse
import json

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc', help="The config.json key for the document you want", required=True)
    return parser.parse_args(args)

def get_google_spreadsheet_data(username, password, key):
    google = gspread.login(username, password)
    spreadsheet = google.open_by_key(key)
    
    return spreadsheet.sheet1.get_all_values()
    
def convert_to_records(data):
    """Transforms a list of lists into a list of dictionaries, where data[0]
       is the header row of data"""
    header, rows = data[0], data[1:]

    def process_cell(s):
        try:
            return int(s)
        except (ValueError, TypeError):
            return s

    def row_to_dict(row):
        converted_row = map(process_cell, row)
        return dict(zip(header, converted_row))

    return map(row_to_dict, rows)      


def spreadsheet_to_json(args):
    arguments = parse_args(args)
    config = json.loads(open("config.json").read())
    this_config = config[arguments.file]
    raw_data = get_google_spreadsheet_data(this_config['username'],
                                           this_config['password'],
                                           this_config['key'])

    print json.dumps(convert_to_records(raw_data))

import sys
import gspread
import argparse
import json


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc', help="The key in the configuration file for "
                                      "the document you want", required=True)
    parser.add_argument('--config', help="The configuration file",
                        required=True)
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
    with open(arguments.config) as f:
        config = json.loads(f.read())
        this_config = config[arguments.doc]
        raw_data = get_google_spreadsheet_data(this_config['username'],
                                               this_config['password'],
                                               this_config['key'])

        sys.stdout.write(json.dumps(convert_to_records(raw_data)))

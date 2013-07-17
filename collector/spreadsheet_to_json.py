import sys
import gspread
import argparse
from list_converter import ListConverter

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help="Google Spreadsheet username",
                        required=True)
    parser.add_argument('--password', help="Google Spreadsheet password. Can be a application specific password",
                        required=True)
    parser.add_argument('--key', help="Google Spreadsheet's key, from the URL",
                        required=True)

    return parser.parse_args(args)
    

def spreadsheet_to_json(args):
    arguments = parse_args(args)

    converter = ListConverter()
    
    gs = gspread.login(arguments.username, arguments.password)
    sh = gs.open_by_key(arguments.key)
    
    data = sh.sheet1.get_all_values()
    
    print converter.to_dict(data)

spreadsheet_to_json(sys.argv[1:])

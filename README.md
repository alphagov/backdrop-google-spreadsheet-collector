[![Build Status](https://travis-ci.org/alphagov/backdrop-google-spreadsheet-collector.png?branch=master)](https://travis-ci.org/alphagov/backdrop-google-spreadsheet-collector)

What is it?
===========

Google Docs Spreadsheet to JSON converter, to be used with
[backdropsend](https://github.com/alphagov/backdropsend).

# Setup

1. Get yourself a virtualenv (optional)
2. `pip install -r requirements_for_tests.txt`

# Running tests

`nosetests`

# Running the app

`./backdrop-google-spreadsheet-collector --username email@example.com --password appspecificpassword --key spreadsheetid`

...where `--username` is your Google login, `--password` is an
[application-specific password](https://security.google.com/settings/security)
and `--key` is the ID (from the URL) of a Google Docs
Spreadsheet that the given user has view access to.

This command will output JSON that can be consumed by other tools, e.g. piped
in to [backdropsend](https://github.com/alphagov/backdropsend).

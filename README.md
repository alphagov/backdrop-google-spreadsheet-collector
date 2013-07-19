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

`./backdrop-google-spreadsheet-collector --doc the_document_i_want`

Create a `config.json` file in this directory that looks a bit like:

    {
      "the_document_i_want": {
        "username": "email@example.com",
        "password": "google-app-specific-password",
        "key": "google-docs-spreadsheet-key"
      }
    }

This command will output JSON that can be consumed by other tools, e.g. piped
in to [backdropsend](https://github.com/alphagov/backdropsend).

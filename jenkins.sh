#!/bin/bash

if [[ -z "$JOB_NAME" ]]; then
    echo -e "\033[31m\$JOB_NAME is not defined!\033[0m"
    exit 128
fi

VIRTUALENV_DIR=/var/tmp/virtualenvs/$(echo ${JOB_NAME} | tr ' ' '-')
PIP_DOWNLOAD_CACHE=/var/tmp/pip_download_cache

basedir=$(dirname $0)

# create empty virtualenv
virtualenv --clear --no-site-packages $VIRTUALENV_DIR
source $VIRTUALENV_DIR/bin/activate

pip install -r requirements_for_tests.txt

nosetests -v --with-xunit --with-coverage --cover-package=collector --xunit-file=$outdir/nosetests.xml
python -m coverage.__main__ xml --include=collector* -o "$outdir/coverage.xml"
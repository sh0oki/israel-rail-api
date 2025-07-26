# Israel Rail API

[![image](https://img.shields.io/pypi/v/israel-rail-api.svg)](https://pypi.org/project/israel-rail-api/)
[![image](https://img.shields.io/pypi/l/israel-rail-api.svg)](https://pypi.org/project/israel-rail-api/)
[![Build status](https://github.com/sh0oki/israel-rail-api/actions/workflows/test.yml/badge.svg)](https://github.com/sh0oki/israel-rail-api/actions/workflows/test.yml)


This is a unofficial wrapping of the API of Israeli Rail network in Python.

Use this script for checking your own train schedule, integrating with Alexa, and so on!

## Installing

Tested with Python 3.8-3.13.

    pip install israel-rail-api

## Usage

    import israelrailapi
    s = israelrailapi.TrainSchedule()
    print(s.query('Tel Aviv University', 'Jerusalem Yitzhak Navon'))

A simple test, to make sure the script is working is included in `schedule.py`:

    python3 schedule.py "tel aviv hahagana" "ben gurion airport" 2023-06-24 0900 

## Contributing

We'd love your contributions! Fire up a (tested!) Pull request, and we'll be happy to approve it.

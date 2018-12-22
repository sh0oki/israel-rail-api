# Israel Rail API
[![Build Status](https://travis-ci.org/sh0oki/israel-rails-api.svg?branch=master)](https://travis-ci.org/sh0oki/israel-rails-api)

This is a unofficial wrapping of the API of Israeli Rail network in Python.

Use this script for checking your own train schedule, integrating with Alexa, and so on!

## Installing
Tested with Python 3.6, should probably work fine with other versions too.

        pip install israel-rail-api

## Usage
        from israelrailapi.schedule import Schedule
        s = Schedule()
        print(s.TrainSchedule('Tel Aviv University', 'Jerusalem Yitzhak Navon'))
        
A simple test, to make sure the script is working is included in `schedule.py`:

        python schedule.py "tel aviv hahagana" "ben gurion airport" 2018-12-24 0900 
        

## Contributing
We'd love your contributions! Fire up a (tested!) Pull request and we'll be happy to approve it.

# Israel Rail API

[![image](https://img.shields.io/pypi/v/israel-rail-api.svg)](https://pypi.org/project/israel-rail-api/)
[![image](https://img.shields.io/pypi/l/israel-rail-api.svg)](https://pypi.org/project/israel-rail-api/)
[![Build status](https://github.com/sh0oki/israel-rail-api/actions/workflows/test.yml/badge.svg)](https://github.com/sh0oki/israel-rail-api/actions/workflows/test.yml)

This is a unofficial wrapping of the API of Israeli Rail network in Python.

Use this script for checking your own train schedule, integrating with Alexa, and so on!

## Installing

Tested with Python 3.8-3.14.

    pip install israel-rail-api

## Usage

    import israelrailapi

    schedule = israelrailapi.TrainSchedule()
    routes = schedule.query('Tel Aviv University', 'Jerusalem Yitzhak Navon')

    for route in routes:
        print(route)

Each returned route contains one or more train segments in `route.trains`.
Every segment is a `TrainRoutePart` with:

* `src` / `dst`: source and destination station ids
* `departure` / `arrival`: scheduled departure and arrival timestamps
* `platform` / `dst_platform`: origin and destination platforms
* `departure_delay`: departure delay in minutes for the segment origin station

Example:

    import israelrailapi

    schedule = israelrailapi.TrainSchedule()
    routes = schedule.query('Tel Aviv HaHagana', 'Ben Gurion Airport', '2026-04-24', '09:00')

    for route in routes:
        for train in route.trains:
            print(
                train.departure,
                train.arrival,
                f"delay={train.departure_delay}m",
            )

CLI example:

    python3 israelrailapi/schedule.py "tel aviv hahagana" "ben gurion airport" 2026-04-24 0900

## Contributing

We'd love your contributions! Fire up a (tested!) Pull request, and we'll be happy to approve it.

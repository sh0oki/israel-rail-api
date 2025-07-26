#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

from setuptools import setup


def make_stations():
    with open(os.path.join(os.path.split(__file__)[0], 'stations.txt'),
              'r', encoding='utf8') as station_file:
        def cleanup_name(n):
            n = n.lower().strip().replace('\'', '').replace('-', ' ')
            return ' '.join(n.split())

        raw = json.load(station_file)['Data']['Data']['CustomPropertys']
        stations = {x.pop('Id'): {l: n[0] for l, n in x.items()} for x in raw}
        # Create reverse dict for indexed query
        station_index = {}
        for st in stations:
            for n in stations[st].values():
                station_index[cleanup_name(n)] = st
    open('israelrailapi/stations.py', 'w', encoding='utf8').write("""#!/usr/bin/env python
# -*- coding: utf-8 -*-

STATIONS = %s
STATION_INDEX = %s
""" % (repr(stations), repr(station_index)))


make_stations()

setup(
    name='israel-rail-api',
    version='0.1.3',
    packages=['israelrailapi'],
    url='https://github.com/sh0oki/israel-rail-api',
    install_requires=['requests',
                      'pytz'],
    license='MIT',
    author='sh0oki',
    description='Israeli Rail unofficial API',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown'
)

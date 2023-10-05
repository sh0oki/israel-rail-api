import time

import requests

from israelrailapi.train_station import station_name_to_id

# API key bundled in main.js of rail.co.il
API_KEY = "4b0d355121fe4e0bb3d86e902efe9f20"

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 ' \
             'Safari/605.1.15'
API_BASE = 'https://israelrail.azurefd.net/rjpa-prod/api/v1'
DEFAULT_HEADERS = {'User-Agent': USER_AGENT,
                   "ocp-apim-subscription-key": API_KEY}


class TrainRoutePart(object):
    def __init__(self, data):
        self.data = data

        self.src = data['orignStation']
        self.dst = data['destinationStation']
        self.arrival = data['arrivalTime']
        self.departure = data['departureTime']
        self.platform = data['originPlatform']
        self.dst_platform = data['destPlatform']

    @staticmethod
    def parse_time(t):
        return time.strptime(t, "%d/%m/%Y %H:%M:%S")

    def __repr__(self):
        return "%s (%s) to %s (%s)" % (
            station_name_to_id(self.src), self.departure, station_name_to_id(self.dst), self.arrival)


class TrainRoute(object):
    def __init__(self, data):
        self.trains = self.parse(data)

        self.start_time = self.trains[0].departure
        self.end_time = self.trains[-1].arrival

    @staticmethod
    def parse(data):
        result = []
        for t in data:
            result.append(TrainRoutePart(t))
        return result

    def __repr__(self):
        return "%d trains in route, starting %s, arriving %s: %s\n" % (len(self.trains),
                                                                       self.start_time,
                                                                       self.end_time,
                                                                       self.trains)


class IsraelRailApi(object):
    def __init__(self, url, params, headers=None):
        self.arguments = None
        if headers is None:
            headers = DEFAULT_HEADERS
        self.url = '/'.join((API_BASE, url))
        self.params = params
        self.headers = headers

    def prepare_arguments(self, arguments):
        unknown_args = arguments.keys() - self.params.keys()
        if len(unknown_args) > 0:
            raise KeyError('Unknown arguments %s' % (unknown_args,))

        for k in self.params:
            if k not in arguments:
                if 'default' in self.params[k]:
                    arguments[k] = self.params[k]['default']
                elif self.params[k]['required'] is not False:
                    raise KeyError('Required argument %s not provided' % (k,))

        return arguments

    def parse(self, result):
        return result

    def request(self, **kwargs):
        self.arguments = self.prepare_arguments(kwargs)
        return self.parse(requests.get(self.url, params=self.arguments, headers=self.headers))


class GetRoutesApi(IsraelRailApi):
    def __init__(self):
        super().__init__('timetable/searchTrainLuzForDateTime',
                         {'fromStation': {}, 'toStation': {},
                          'date': {},
                          'hour': {'default': '09:00'},
                          'scheduleType': {'default': 1},
                          'systemType': {"default": 2},
                          "languageId": {"default": "English"}
                          })

    def parse(self, raw_result):
        raw_result.raise_for_status()
        result = raw_result.json()['result']
        size = result['numOfResultsToShow']
        index = result['startFromIndex']

        routes = result['travels'][index: index + size]
        return [TrainRoute(r['trains']) for r in routes]

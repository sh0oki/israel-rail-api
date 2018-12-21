import requests
import time

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 ' \
             'Safari/537.36'
API_BASE = 'https://www.rail.co.il/apiinfo/api/Plan'
DEFAULT_HEADERS = {'User-Agent': USER_AGENT}


class TrainRoutePart(object):
    def __init__(self, data):
        self.data = data

        self.src = data['OrignStation']
        self.dst = data['DestinationStation']
        self.arrival = data['ArrivalTime']
        self.departure = data['DepartureTime']
        self.platform = data['Platform']
        self.dst_platform = data['DestPlatform']

    @staticmethod
    def parse_time(t):
        return time.strptime(t, "%d/%m/%Y %H:%M:%S")

    def __repr__(self):
        return "%s (%s) to %s (%s)" % (self.src, self.departure, self.dst, self.arrival)


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
    def __init__(self, url, params, headers=DEFAULT_HEADERS):
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
        arguments = self.prepare_arguments(kwargs)
        return self.parse(requests.get(self.url, params=arguments, headers=self.headers))


class GetRoutesApi(IsraelRailApi):
    def __init__(self):
        super().__init__('GetRoutes',
                         {'OId': {}, 'TId': {},
                          'Date': {},
                          'Hour': {'default': '0900'},
                          'isGoing': {'default': 'true', 'required': False}
                          })

    def parse(self, raw_result):
        raw_result.raise_for_status()
        routes = raw_result.json()['Data']['Routes']
        return [TrainRoute(r['Train']) for r in routes]

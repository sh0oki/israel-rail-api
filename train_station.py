import logging
import os
import json
from jsoncomment import JsonComment


class TrainStationIndex(object):
    def __init__(self, station_file=os.path.join(os.path.split(__file__)[0], 'stations.txt')):
        with open(station_file, encoding='utf8') as station_file:
            raw = JsonComment(json).load(station_file)['Data']['Data']['CustomPropertys']
            self.stations = {x.pop('Id'): {l: n[0] for l, n in x.items()} for x in raw}
            # Create reverse dict for indexed query
            self.station_index = {}
            for st in self.stations:
                for n in self.stations[st].values():
                    self.station_index[self.cleanup_name(n)] = st
        logging.debug(self.station_index)

    @staticmethod
    def cleanup_name(n):
        n = n.lower().strip().replace('\'', '').replace('-', ' ')
        return ' '.join(n.split())

    def lookup(self, n):
        return self.station_index[self.cleanup_name(n)]


if __name__ == '__main__':
    print(TrainStationIndex().station_index)


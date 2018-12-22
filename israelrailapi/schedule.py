import logging
import time
import sys

from israelrailapi.train_station import TrainStationIndex
from israelrailapi.api import GetRoutesApi


class TrainSchedule(object):
    def __init__(self):
        self.stations = TrainStationIndex()

    def translate_station(self, station_name):
        # Station name can be: int (station id), string (station id), string (station name)
        station_name = str(station_name).lower()
        if station_name in self.stations.stations:
            return self.stations.stations[station_name]

        return self.stations.lookup(station_name)

    def query(self, src_station, dst_station, start_date=None, start_hour=None):
        src_station = self.translate_station(src_station)
        dst_station = self.translate_station(dst_station)
        if start_date is None:
            start_date = time.strftime("%Y-%m-%d")
        if start_hour is None:
            start_hour = "09:00"
        start_date = start_date.strip().replace('-', '').replace('/', '').replace('.', '')
        start_hour = start_hour.strip().replace(':', '')

        logging.info("Query: %s->%s (%s %s)" % (src_station, dst_station,
                                                start_date, start_hour))
        result = GetRoutesApi().request(OId=src_station, TId=dst_station,
                                        Date=start_date, Hour=start_hour)
        logging.info(result)
        return result


if '__main__' == __name__:
    logging.basicConfig(level=logging.DEBUG)
    t = TrainSchedule()
    if len(sys.argv) >= 4:
        t.query(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: %s <src> <dst> <YYYY-MM-DD> <hh:mm>" % (sys.argv[0], ))

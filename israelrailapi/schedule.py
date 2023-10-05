import logging
import sys
import time

from israelrailapi.api import GetRoutesApi
from israelrailapi.train_station import translate_station


class TrainSchedule(object):
    @staticmethod
    def query(src_station, dst_station, start_date=None, start_hour=None):
        src_station = translate_station(src_station)
        dst_station = translate_station(dst_station)
        if start_date is None:
            start_date = time.strftime("%Y-%m-%d")
        if start_hour is None:
            start_hour = "09:00"
        start_date = start_date.strip().replace('-', '').replace('/', '').replace('.', '')
        start_hour = start_hour.strip().replace(':', '').replace('-', '')
        start_hour = f"{start_hour[:2]}:{start_hour[2:]}"
        start_date = f"{start_date[:4]}-{start_date[4:6]}-{start_date[6:8]}"

        logging.info("Query: %s->%s (%s %s)" % (src_station, dst_station,
                                                start_date, start_hour))
        result = GetRoutesApi().request(fromStation=src_station, toStation=dst_station,
                                        date=start_date, hour=start_hour)
        logging.info(result)
        return result


if '__main__' == __name__:
    logging.basicConfig(level=logging.DEBUG)
    t = TrainSchedule()
    if len(sys.argv) == 5:
        q = t.query(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        print(q)
    else:
        print("Usage: %s <src> <dst> <YYYY-MM-DD> <hh:mm>" % (sys.argv[0],))

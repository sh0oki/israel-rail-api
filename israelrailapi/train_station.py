import logging

try:
    from israelrailapi.stations import STATIONS, STATION_INDEX
except ImportError:
    logging.warning("Unable to load station list")
    from stations import STATIONS, STATION_INDEX


def cleanup_name(n):
    n = n.lower().strip().replace('\'', '').replace('-', ' ')
    return ' '.join(n.split())


def lookup_station(n):
    return STATION_INDEX[cleanup_name(n)]


def translate_station(station_name):
    # Station name can be: int (station id), string (station id), string (station name)
    station_name = str(station_name).lower()
    if station_name in STATIONS:
        return STATIONS.stations[station_name]

    return lookup_station(station_name)


def station_name_to_id(lookup_name, default_language='Eng'):
    for station_id in STATIONS:
        if any(name == str(lookup_name) for name in STATIONS[station_id]):
            return station_id
    return lookup_name

if __name__ == '__main__':
    print(STATION_INDEX)

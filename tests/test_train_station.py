import unittest
from israelrailapi import train_station

KNOWN_STATIONS = {'Jerusalem- yitzhak navon': 680, 'Dimona': 7500}


class ApiTest(unittest.TestCase):
    def test_station_lookup(self):
        # Testing known stations, not ideal but...
        for name, station_id in KNOWN_STATIONS.items():
            self.assertEqual(str(station_id), train_station.lookup_station(name))

    def failed_station_lookup(self):
        with self.assertRaises(KeyError):
            train_station.lookup_station('NY Penn')

        with self.assertRaises(KeyError):
            train_station.lookup_station['-700']


if __name__ == '__main__':
    unittest.main()

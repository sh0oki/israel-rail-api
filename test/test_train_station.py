import unittest
import train_station

KNOWN_STATIONS = {'Jerusalem- yitzhak navon': 680, 'Dimona': 7500}


class ApiTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.stations = train_station.TrainStationIndex()

    def test_station_lookup(self):
        # Testing known stations, not ideal but...
        for name, station_id in KNOWN_STATIONS.items():
            self.assertEqual(str(station_id), self.stations.lookup(name))

    def failed_station_lookup(self):
        with self.assertRaises(KeyError):
            self.stations.lookup('NY Penn')

        with self.assertRaises(KeyError):
            self.stations.stations['-700']


if __name__ == '__main__':
    unittest.main()

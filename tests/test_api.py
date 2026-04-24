import unittest
from israelrailapi import api

TEST_API_NAME = 'MyApi'
TEST_PARAMS = {'required': {},
               'notRequired': {'required': False},
               'default': {'default': 5}
               }


def _route_part_data(eta_diff_times=...):
    data = {
        'orignStation': 3600,
        'destinationStation': 3700,
        'arrivalTime': '01/01/2026 10:30:00',
        'departureTime': '01/01/2026 10:00:00',
        'originPlatform': 1,
        'destPlatform': 2,
    }
    if eta_diff_times is not ...:
        data['etaDiffTimes'] = eta_diff_times
    return data


class ApiTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.rail_test = api.IsraelRailApi(TEST_API_NAME, TEST_PARAMS)

    def test_setup(self):
        self.assertEqual(self.rail_test.url, api.API_BASE + "/" + TEST_API_NAME)

    def test_request_args(self):
        result = self.rail_test.prepare_arguments({'required': 'Hello'})
        self.assertEqual(result, {'required': 'Hello', 'default': 5})
        with self.assertRaises(KeyError):
            self.rail_test.prepare_arguments({'notRequired': 'Hello'})

        with self.assertRaises(KeyError):
            self.rail_test.prepare_arguments({'required': 'Hello', 'notRequired': 'Hello', 'random': 7})


class TrainRoutePartTest(unittest.TestCase):
    def test_departure_delay_matching_station(self):
        data = _route_part_data(eta_diff_times=[
            {'stationId': 9999, 'difMin': 2},
            {'stationId': 3600, 'difMin': 5},
        ])
        part = api.TrainRoutePart(data)
        self.assertEqual(part.departure_delay, 5)

    def test_departure_delay_no_matching_station(self):
        data = _route_part_data(eta_diff_times=[{'stationId': 9999, 'difMin': 7}])
        part = api.TrainRoutePart(data)
        self.assertEqual(part.departure_delay, 0)

    def test_departure_delay_empty_list(self):
        data = _route_part_data(eta_diff_times=[])
        part = api.TrainRoutePart(data)
        self.assertEqual(part.departure_delay, 0)

    def test_departure_delay_missing_key(self):
        data = _route_part_data()
        part = api.TrainRoutePart(data)
        self.assertEqual(part.departure_delay, 0)


if __name__ == '__main__':
    unittest.main()

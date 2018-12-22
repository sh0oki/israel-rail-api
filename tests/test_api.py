import unittest
from israelrailapi import api

TEST_API_NAME = 'MyApi'
TEST_PARAMS = {'required': {},
               'notRequired': {'required': False},
               'default': {'default': 5}
               }


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


if __name__ == '__main__':
    unittest.main()

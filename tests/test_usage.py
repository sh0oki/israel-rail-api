import unittest
import israelrailapi

TEST_API_NAME = 'MyApi'
TEST_PARAMS = {'required': {},
               'notRequired': {'required': False},
               'default': {'default': 5}
               }


class ApiTest(unittest.TestCase):

    def test_usage(self):
        s = israelrailapi.TrainSchedule()

        from_date = "2023-06-24"
        from_time = "0900"

        q = s.query("tel aviv hashalom", "hod hasharon sokolov", from_date, from_time)

if __name__ == '__main__':
    unittest.main()

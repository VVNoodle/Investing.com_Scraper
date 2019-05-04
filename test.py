from service import app
import unittest
import sys
import json


class FlaskBookshelfTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client

        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get(
            '/commodity?start_date=2019-04-17&end_date=2019-05-01&commodity_type=gold')
        # assert the response data
        self.obj = json.loads(result.data.decode())

        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_should_have_mean_and_var(self):
        self.assertTrue(self.obj["mean"] is not None)
        self.assertIs(type(self.obj["mean"]), float)
        self.assertTrue(self.obj["variance"] is not None)
        self.assertIs(type(self.obj["variance"]), float)

    def test_should_have_data(self):
        # assert the response data
        self.assertTrue(self.obj["data"] is not None)
        self.assertIs(type(self.obj["data"]), dict)

    def test_mean(self):
        # assert the response data
        data = self.obj["data"]
        mean = 0
        for date, price in data.items():
            mean += price
        mean /= len(data)
        self.assertEqual(mean, self.obj["mean"])


if __name__ == "__main__":
    print("Testing...", file=sys.stderr)
    unittest.main()

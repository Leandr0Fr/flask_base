import os, sys
import unittest

current_route = os.path.dirname(os.path.abspath(__file__))
route_src = os.path.abspath(os.path.join(current_route, '..'))
sys.path.append(route_src)

from app import app
class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ping_endpoint(self):
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
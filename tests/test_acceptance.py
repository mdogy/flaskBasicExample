
import unittest
import requests

""" Acceptance tests should test the project as a running server, preferably deployed, with running database. These test the server just as a user interacting with it.

These tests may be slower.
"""

url= 'http://localhost:5000'

class TestLocalAcceptance(unittest.TestCase):



    def test_local_page_5000(self):
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)


import unittest
import requests

url= 'http://localhost:5000'

class TestLocalAcceptance(unittest.TestCase):


    def test_local_page_5000(self):
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

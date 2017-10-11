""" Acceptance tests should test the project as a running server, preferably deployed, with running database. These test the server just as a user interacting with it.

These tests may be slower.
"""
import unittest
import requests
from bs4 import BeautifulSoup

url= 'http://localhost:5000'

class TestLocalAcceptance(unittest.TestCase):

    def test_page_exists(self):
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_form_on_page(self):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        self.assertIsNotNone(soup.form)
        self.assertEqual(soup.label.text.strip(), "Text to Hash")

    def test_submit_form(self):
        texthash = "6dd76dd3adf4dba52acf81d227a6a9a525b0140126015534d11338ca"
        text4hash = "Doggo ate my shoes."
        payload = {"text4hash":text4hash}
        r = requests.get(url, params=payload)
        soup = BeautifulSoup(r.text, "html.parser")
        self.assertEqual(soup.div.text.strip(), "Hash: "+texthash)

""" Integration tests are not as isolated as unit tests but may not be full
acceptance tests. In this context we are checking that your code works with
flask, sqlalchemy and the other modules."""
import unittest
import mathapp
from bs4 import BeautifulSoup

class TestMathAppInt(unittest.TestCase):

    def setUp(self):
        """Will need a text client for all these tests"""
        self.app = mathapp.app.test_client()

    def test_index_page_h1(self):
        """Just checking h1 field correct"""
        rv = self.app.get('/')
        soup = BeautifulSoup(rv.data, "html.parser")
        self.assertEqual(soup.h1.text.strip(), 'Math App')

    def test_index_title(self):
        """Just checking title field correct. Variable in base template."""
        rv = self.app.get('/')
        soup = BeautifulSoup(rv.data, "html.parser")
        self.assertEqual(soup.title.text.strip(), 'Math App homepage')

    def test_submit_form(self):
        """Same as acceptance test. Can check even when server not running."""
        texthash = "6dd76dd3adf4dba52acf81d227a6a9a525b0140126015534d11338ca"
        text4hash = "Doggo ate my shoes."
        payload = {"text4hash": text4hash}
        rv = self.app.get("/", query_string=payload)
        soup = BeautifulSoup(rv.data, "html.parser")
        self.assertEqual(soup.div.text.strip(), "Hash: " + texthash)

    def test_submit_placeholder(self):
        """Checking placeholder attribute of textarea set with query_string."""
        rv = self.app.get('/')
        soup = BeautifulSoup(rv.data, "html.parser")
        self.assertEqual(soup.textarea.attrs['placeholder'],
            'Type your text here.')
        text4hash = "Doggo ate my shoes."
        payload = {"text4hash": text4hash}
        rv = self.app.get("/", query_string=payload)
        soup = BeautifulSoup(rv.data, "html.parser")
        self.assertEqual(soup.textarea.attrs['placeholder'],
            text4hash)

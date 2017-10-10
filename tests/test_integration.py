""" Integration tests are not as isolated as unit tests but may not be full acceptance tests. In this context we are checking that your code works with flask, sqlalchemy and the other modules."""
import unittest
import mathapp
from bs4 import BeautifulSoup

class TestMathAppInt(unittest.TestCase):

    def setUp(self):
        self.app = mathapp.app.test_client()

    def test_index_page_h1(self):
        rv = self.app.get('/')
        soup = BeautifulSoup(rv.data, "html.parser")
        self.assertEqual(soup.h1.text.strip(), 'Math App')

    def test_index_title(self):
        rv = self.app.get('/')
        soup = BeautifulSoup(rv.data, "html.parser")
        self.assertEqual(soup.title.text.strip(), 'Mathapp homepage')

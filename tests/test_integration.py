import unittest
import mathapp

class TestMathAppInt(unittest.TestCase):

    def setUp(self):
        self.app = mathapp.app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data, b'Hello World!')

import unittest
import mathapp


class TestMathAppUnit(unittest.TestCase):

    def test_index_hello(self):
        self.assertEqual('Hello World!', mathapp.routes.index())

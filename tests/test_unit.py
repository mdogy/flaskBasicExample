"""Pure unittest test your code isolated from all other code. They should patch internal libraries and mock whenever needed. """
import unittest
import mathapp
from unittest.mock import patch

class TestMathAppUnit(unittest.TestCase):

    def test_index_hello(self):
        with patch('mathapp.routes.render_template') as render_template:
            mathapp.routes.index()
            self.assertTrue(render_template.called)
            call_args = render_template.call_args
            template_name = call_args[0][0]
            self.assertEqual(template_name, "index.html")

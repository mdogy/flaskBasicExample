"""Pure unittest test your code isolated from all other code. They should patch internal libraries and mock whenever needed. """
import unittest
import mathapp
from unittest.mock import patch, DEFAULT, Mock

class TestMathAppUnit(unittest.TestCase):

    def test_index_gets_index_template(self):
        with patch.multiple('mathapp.routes',
                            request=DEFAULT,
                            render_template=DEFAULT,
                            hashlib=DEFAULT) as mock_funcs:
            mathapp.routes.index()
            render_template = mock_funcs['render_template']
            self.assertTrue(render_template.called)
            call_args = render_template.call_args
            template_name = call_args[0][0]
            self.assertEqual(template_name, "index.html")

    def test_index_simple_get(self):
        with patch.multiple('mathapp.routes',
                            request=DEFAULT,
                            render_template=DEFAULT,
                            hashlib=DEFAULT) as mock_funcs:
            request = mock_funcs['request']
            request.args = None
            mathapp.routes.index()
            render_template = mock_funcs['render_template']
            self.assertTrue(render_template.called)
            call_args = render_template.call_args
            current_text = call_args[1]['current_text']
            self.assertEqual(current_text, "Type your text here.")
            hashtext = call_args[1]['hash']
            self.assertIsNone(hashtext)

    def test_index_get_with_query(self):
        with patch.multiple('mathapp.routes',
                            request=DEFAULT,
                            render_template=DEFAULT,
                            hashlib=DEFAULT) as mock_funcs:
            request = mock_funcs['request']
            hashlib = mock_funcs['hashlib']
            render_template = mock_funcs['render_template']
            doggo_text = "Doggo ate my shoes."
            hash_text = "12414210481"
            request.args.get.return_value = doggo_text
            hashlib.sha224.return_value = Mock()
            hashlib.sha224.return_value.hexdigest.return_value = hash_text
            mathapp.routes.index()
            text4hash = request.args.get.call_args[0][0]
            self.assertEqual(text4hash,'text4hash')
            self.assertTrue(render_template.called)
            call_args = render_template.call_args
            current_text = call_args[1]['current_text']
            self.assertEqual(current_text, doggo_text)
            hashtext = call_args[1]['hash']
            self.assertEqual(hashtext,hash_text)

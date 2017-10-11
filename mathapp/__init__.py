"""Implements a basic flask app that provides hashes of text."""
from flask import Flask
app = Flask(__name__)  # pylint: disable=invalid-name
import mathapp.routes  # pylint: disable=wrong-import-position

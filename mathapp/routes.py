"""Routes for flask app."""  # pylint: disable=cyclic-import
import hashlib
from flask import render_template
from flask import request
from mathapp import app


@app.route('/', methods=['GET'])
def index():
    """View displays or processes get form. Hashes and displays input text."""
    hashtext = None
    current_text = None
    if request.args:
        current_text = request.args.get('text4hash')
    if current_text:
        hashtext = hashlib.sha224(current_text.encode()).hexdigest()
    else:
        current_text = "Type your text here."
    return render_template("index.html",
                           current_text=current_text,
                           hash=hashtext,
                           page_title="Math App homepage")

from mathapp import app
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html",page_title="Mathapp homepage")

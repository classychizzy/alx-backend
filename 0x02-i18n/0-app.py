#!/usr/bin/env python3
"""
a flask app that returns hello world
"""


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index() -> str:
    """ a function that returns a template"""
    return render_template('0-index.html', title='Home')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

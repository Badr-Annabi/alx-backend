#!/usr/bin/env python3
"""
This file we'll Create a single
/ route and an index.html template that simply outputs
“Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>)
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """renders 0-indec.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

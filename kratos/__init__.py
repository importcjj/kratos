# -*- coding:utf-8 -*-

import flask
from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong!'


@app.route('/whoami')
def whoami():
    return '<h1>Kratos</h1>'


@app.errorhandler(404)
def page_not_found():
    return flask.render_template('404.html')

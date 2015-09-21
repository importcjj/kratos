# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong!'


@app.route('/whoami')
def whoami():
    return '<h1>Kratos</h1>'

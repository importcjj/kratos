# -*- coding:utf-8 -*-

import flask
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
filehandler = RotatingFileHandler('kratos.log', mode='a')
filehandler.setLevel(logging.NOTSET)
app.logger.addHandler(filehandler)


@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html')

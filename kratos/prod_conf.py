
import logging
from logging.handlers import RotatingFileHandler

filehandler = RotatingFileHandler('/data/log/kratos.log', mode='a')
filehandler.setLevel(logging.NOTSET)


def prod_configure(app):
    app.logger.addHandler(filehandler)

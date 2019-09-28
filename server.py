#!/usr/bin/env python3

from flask import Flask
import logging
import os

DEBUG = False
app_log = logging.getLogger('ycj')
app = Flask(__name__)


def setup_paths():
    for req_path in ('logs/'):
        try:
            os.mkdir(req_path)
        except FileExistsError:
            pass


def setup_logging():
    if DEBUG:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    # send messages to a rotated log file - rotated every monday
    flask_handler = logging.handlers.TimedRotatingFileHandler('./logs/flask.log', when='W0')
    flask_handler.setFormatter(formatter)
    flask_handler.setLevel(loglevel)
    app.logger.addHandler(flask_handler)
    app.logger.setLevel(loglevel)
    app_handler = logging.handlers.TimedRotatingFileHandler('./logs/app.log', when='W0')
    app_handler.setFormatter(formatter)
    app_handler.setLevel(loglevel)
    app_log.addHandler(app_handler)
    app_log.setLevel(loglevel)


@app.route('/')
def index():
    # load index.html through the template engine and fire it at the user
    return "hello"

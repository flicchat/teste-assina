from flask import Flask
from flask_cors import CORS

from consulta.ext import configuration


def minimal_app(**config):
    app = Flask(__name__)
    CORS(app)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    from consulta import models
    return app

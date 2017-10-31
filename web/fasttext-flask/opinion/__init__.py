# -*- coding: utf-8 -*-

from flask import Flask
from opinion.emotion.views import mod as emotionModule

def create_app():
    app = Flask(__name__)
    # app.config.from_object('config')
    # Create modules
    app.register_blueprint(emotionModule)
    return app


from flask import Flask
import os


def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.secret_key = os.environ.get("FLASK_SECRET_KEY")
    return app

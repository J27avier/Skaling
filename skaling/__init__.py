import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask

from skaling import pages, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(dotenv_values())

    database.init_app(app)

    app.register_blueprint(pages.bp)

    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")

    return app

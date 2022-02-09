# import the Flask function/class
from flask import Flask
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def create_app(test_config = None):
    # configure application
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    # strict_slashes set to false makes trailing slashes on route names optional(?)
    app.config.from_mapping(
        SECRET_KEY = getenv('SECRET_KEY')
    )

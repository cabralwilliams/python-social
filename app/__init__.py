# import the Flask function/class
from flask import Flask

def create_app(test_config = None):
    # configure application
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    # strict_slashes set to false makes trailing slashes on route names optional(?)

# import the Flask function/class
from flask import Flask
from os import getenv
from dotenv import load_dotenv
from app.utils import filters
from app.routes import api, home, dashboard
from app.db import init_db

load_dotenv()

def create_app(test_config = None):
    # configure application
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    # strict_slashes set to false makes trailing slashes on route names optional(?)
    app.config.from_mapping(
        SECRET_KEY = getenv('SECRET_KEY')
    )

    # register routes
    app.register_blueprint(api)
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    init_db(app)

    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    return app

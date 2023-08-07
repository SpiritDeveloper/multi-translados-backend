# Import modules
from os import getenv
from flask import Flask
import coloredlogs, logging
from flask_cors import CORS
from flask_smorest import Api
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# load configuration .env
load_dotenv()
db = SQLAlchemy()

# configuration
class Config:
    ENV = getenv("SERVER_ENV")
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(
        getenv("DATABASE_NAME"),
        getenv("DATABASE_USER"),
        getenv("DATABASE_PASSWORD"),
        getenv("DATABASE_HOST"),
        getenv("DATABASE_PORT"),
        getenv("DATABASE_DB"),
    )
    SQLALCHEMY_POOL_SIZE = 10000000
    SQLALCHEMY_MAX_OVERFLOW = 10000000
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    TESTING = False
    JSON_SORT_KEYS = False
    API_VERSION = 0.1
    API_TITLE = "API MultiTranslados"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_URL_PREFIX = "/api"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    API_SPEC_OPTIONS = {
        "components": {
            "securitySchemes": {
                "Bearer Auth": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "Authorization",
                    "bearerFormat": "JWT",
                    "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the access token",
                }
            }
        },
        "info": {
            "description": "API Multitranslados",
            "contact": {"email": "roberto.espiritu@platimex.com.mx"},
            "license": {
                "name": "Development MultiTranslados",
                "url": "https://gist.github.com/SpiritDeveloper",
            },
        },
    }

    SECRET_KEY = getenv("SECRET_KEY")

def create_app():
    # Flask start
    app = Flask(__name__)
    app.debug = True

    # logs configuration
    logging.basicConfig(format="%(asctime)s %(message)s")
    coloredlogs.install(level="WARNING", logger=logging.getLogger(), isatty=True)
    coloredlogs.install(level="INFO", logger=logging.getLogger(), isatty=True)

    # Add configuration
    app.config.from_object(Config)

    # try create all models
    db.init_app(app)

    with app.app_context():
        from .controllers import (
            main,
            security,
            area,
            position
        )
        api = Api(app)

        # register modules
        api.register_blueprint(main)
        api.register_blueprint(security)
        api.register_blueprint(area)
        api.register_blueprint(position)


        # register cors
        CORS(app, supports_credentials=True)
        CORS(main, supports_credentials=True)
        CORS(security, supports_credentials=True)
        CORS(area, supports_credentials=True)
        CORS(position, supports_credentials=True)

        for path, items in api.spec._paths.items():
            for method in items.keys():
                try:
                    if api.spec._paths[path][method].get("authorize", False):
                        api.spec._paths[path][method]["security"] = [{"Bearer Auth": []}]
                except:
                    pass
        
        db.create_all()  # Create database tables for our data models
        return app

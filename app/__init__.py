from flask import Flask
from .db import db
from .ext import ma, migrate
from flasgger import Swagger
from flask_cors import CORS
from .user.controller.user_controller import user
from .auth.controller.auth_controller import auth

prefix="/prisma.dev"

def create_app(settings_module):
    app = Flask(__name__)
    
    app.config.from_object(settings_module)
    host = app.config.get("SITE_HOST")
    
    swagger_template = {
        "info": {
            'title': 'Api Python Test',
            'version': '0.1',
            'description': 'This document contains the list of API services '
                           'with Python.',
        },
        "host": host,
        "schemes":["http" , "https"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Authorization: Bearer {token}"
            }   
        },
        "security": [
            {
                "Bearer": []
            }
        ]
    }
    CORS(app, supports_credentials=False)
    Swagger(app, template=swagger_template)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)
    
    #* BLUEPRINTS
    app.register_blueprint(user, url_prefix=f"{prefix}/users")
    app.register_blueprint(auth, url_prefix=f"{prefix}/login")
    return app
    
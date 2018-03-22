# project/server/__init__.py


import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


# instantiate the extensions
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder='../client/templates',
        static_folder='../client/static'
    )

    # set config
    app_settings = os.getenv(
        'APP_SETTINGS', 'project.server.config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # set up extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # register blueprints
    from project.server.main.views import main_blueprint
    app.register_blueprint(main_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})

    return app

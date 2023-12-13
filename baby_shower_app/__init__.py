import os

from flask import Flask

from . import db
from . import gift_inspo


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='postgresql://smwmbakbnpuzdw:1f46e4244a901918e95c48369b321c03b405d297f7e879edbcbe3c35aa8b08fe@ec2-3-210-173-88.compute-1.amazonaws.com;5432/dcpf970dfp3rdn',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'

    db.init_app(app)
    db.init_db()

    app.register_blueprint(gift_inspo.bp)

    return app

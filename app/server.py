import os
import logging
import logging.config

import tornado.ioloop
import tornado.web
from tornado.options import options

from sklearn.externals import joblib

from app.settings import MODEL_DIR, AUTH_KEY, AUTH_SECRET
from app.auth_handler import setup_auth_controller, AuthTokenHandler, AuthTestHandler
from app.handler import IndexHandler, IrisPredictionHandler


MODELS = {}


def load_model(pickle_filename):
    return joblib.load(pickle_filename)


def main():

    # Get the Port and Debug mode from command line options or default in settings.py
    options.parse_command_line()


    # create logger for app
    # logging.config.dictConfig(LOG_SETTINGS)
    logger = logging.getLogger('app')
    logger.setLevel(logging.INFO)

    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT)

    # Load ML Models
    logger.info("Loading IRIS Prediction Model...")
    MODELS["iris"] = load_model(os.path.join(MODEL_DIR, "iris", "model.pkl"))

    # # Setup Auth Controller
    # auth_controller = setup_auth_controller(AUTH_KEY, AUTH_SECRET, auth_url="/auth/token")
    #     (r'/auth/token', AuthTokenHandler, dict(controller=auth_controller)),
    #     (r'/auth/test', AuthTestHandler, dict(controller=auth_controller)),

    urls = [
        (r"/$", IndexHandler),
        (r"/api/iris/(?P<action>[a-zA-Z]+)?", IrisPredictionHandler,
            dict(model=MODELS["iris"]))
    ]

    # Create Tornado application
    application = tornado.web.Application(
        urls,
        debug=options.debug,
        autoreload=options.debug)

    # Start Server
    logger.info("Starting App on Port: {} with Debug Mode: {}".format(options.port, options.debug))
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



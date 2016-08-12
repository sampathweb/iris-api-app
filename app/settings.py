"""
Appliction configuration settings
"""
import os

from tornado.options import define

define("debug", default=True, help="Debug settings")
define("port", default=9000, help="Port to run the server on")

_CUR_DIR = os.path.dirname(os.path.realpath(__file__))
MODEL_DIR = os.path.join(_CUR_DIR, "..", "models")
LOG_DIR = os.path.join(_CUR_DIR, "..", "logs")

# Auth Settings
AUTH_KEY = "admin"
AUTH_SECRET = "pydata"

MAX_MODEL_THREAD_POOL = 10

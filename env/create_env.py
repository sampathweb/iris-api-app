#! /usr/bin/env python

"""Sets up the env"""

from __future__ import print_function, absolute_import
import os
from subprocess import call

ENV_ROOT = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(ENV_ROOT)
VENV_NAME = os.environ.get("VENV_NAME", "venv")
VENV_PATH = os.path.join(ENV_ROOT, VENV_NAME)

CONDA_REQUIREMENTS_PATH = os.path.join(APP_ROOT, "requirements_conda.txt")
PIP_REQUIREMENTS_PATH = os.path.join(APP_ROOT, "requirements_pip.txt")

if not os.path.exists(VENV_PATH):
    # create virtualenv
    print("Creating virtual environment at %s" % VENV_PATH)
    call("conda create -p {} python=3 --yes".format(VENV_PATH), shell=True)

print("Please Activate the Environment: source activate env/venv (in Mac/Linux) & activate env/venv (Windows)")
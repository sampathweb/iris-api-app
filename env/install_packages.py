from __future__ import print_function, absolute_import
import os
from subprocess import call

ENV_ROOT = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(ENV_ROOT)
VENV_NAME = os.environ.get("VENV_NAME", "venv")
VENV_PATH = os.path.join(ENV_ROOT, VENV_NAME)
VENV_BIN_PATH = os.path.join(VENV_PATH, "bin")
ACTIVATE_PATH = os.path.join(VENV_BIN_PATH, "activate")

CONDA_REQUIREMENTS_PATH = os.path.join(APP_ROOT, "requirements_conda.txt")
PIP_REQUIREMENTS_PATH = os.path.join(APP_ROOT, "requirements_pip.txt")



# Activate the virtual environment
# call("source activate venv", shell=True)

# update any python packages
print("Installing and/or updating requirements...")
call("conda install --file %s --yes" % CONDA_REQUIREMENTS_PATH,
     shell=True)
call("pip install -r %s" % PIP_REQUIREMENTS_PATH,
     shell=True)

print("Virtual Environment is setup and activated.  "
      "In future, run 'source activate env/venv (in Mac/Linix) and activate env/venv (in Windows)' to Activate it")

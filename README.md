# Sample IRIS API App

## Setup Environment on Local Machine

### Installation

```
cookiecutter https://github.com/sampathweb/cc-api-app

cd <repo>  # cd iris-api-app

# Install Packages
python env/create_env.py
source activate env/venv  # Windows users: activate env/venv
python env/install_packages.py

# Build the Model
python ml_src/build_model.py

# Run the App
python run.py
````

### Test App


1. Open Browser:  http://localhost:9000 (App is Live!)

2. Test API:

curl -i http://localhost:9000/api/iris/predict -X POST -d '{ "sepal_length": 2, "sepal_width": 5, "petal_length": 3, "petal_width": 4}'


Api works!

### Push code to your own git repo.

Make sure you are in the Application directory

```
git init
git add --all
git commit -m "first commit"
git remote add origin https://github.com/<your github username>/<remote repo name>.git
git push --set-upstream origin master

```


## Deploy Steps for AWS Ubuntu 14.04 LTS EC2 Instance

### Login to AWS Instance:

`ssh -i <your AWS Pem key file> ubuntu@<aws ip>`


### Install Python / Git

```
sudo apt-get update
sudo apt-get upgrade

# Install GIT
sudo apt-get install git

# Install Anaconda (Miniconda)
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh

# To update the path (Make sure you said Yes when it asked to update path in the Miniconda install steps)
source ~/.bashrc
```

### Download App Source Code:
```

git clone https://github.com/sampathweb/iris-api-app.git


cd iris-api-app
python env/create_env.py
source activate env/venv
python env/install_packages.py

python ml_src/build_model.py
python run.py (Confirm that App is running)


sudo apt-get install supervisor
sudo vi /etc/supervisor/conf.d/iris-api.conf
<press i insert mode>

[program:iris-api-app]
autorestart = true
command = /home/ubuntu/iris-api-app/env/venv/bin/python /home/ubuntu/iris-api-app/run.py --debug=False --port=80
numprocs = 1
startsecs = 10
stderr_logfile = /var/log/supervisor/iris-api-app.log
stdout_logfile = /var/log/supervisor/iris-api-app.log
# stderr_logfile = syslog
# stdout_logfile = syslog
environment = PYTHONPATH="/home/ubuntu/iris-api-app/env/bin/"

<escape :wq>

sudo supervisorctl reload

<Your APP is live now>
```

### Test the App

1. Open Browser:  http://<AWS IP> (App is Live!)

2. Test API:

curl -i http://<aws ip address>/api/iris/predict -X POST -d '{ "sepal_length": 2, "sepal_width": 5, "petal_length": 3, "petal_width": 4}'


Congratulations you have deployed your App
```

## Credits:

Template from https://github.com/sampathweb/cc-api-app


### The End.
# TwistR-Backend
Django REST API for TwistR (Twitter with a twist)

## Setup Instructions

### Python Tools
[Source](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-18-04)

Open up your favorite terminal (ex. Bash, Git Bash)

Run the following commands in a top-level directory such as `~`, or wherever you keep your work. 

Check the version of python by running
```
python3 -V
```

If this returns `Python 3.5.0` or higher, you should be aiiiight.
If python3 isn't installed, or you think the version isn't high enough, try installing python3 through the command line using apt, or talk to Charlene :)

To manage software packages for Python, install pip, a tool that will install and manage programming packages we may want to use in our development projects. We'll mostly just need this to install Django.
```
sudo apt install -y python3-pip
```

Install a few more things for a robust dev environment... (Note: not sure if we need these if not planning on modifying any backend code, but I haven't tried running the server, etc. without them installed)
```
sudo apt install build-essential libssl-dev libffi-dev python-dev
```

Now you should have all the tools to start python programming! Yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay.

### Setup Project 

Navigate to wherever you want to keep the backend repo, and run
```
git clone https://github.com/charlorr/TwistR-Backend.git
```

Move into the repo
``` 
cd TwistR-Backend/
```

To make a python virtual environment, run
```
python3 -m venv ./env
```

Then start it with,
```
source env/bin/activate
```

Then install django.
```
pip install django djangorestframework django-cors-headers
```

...

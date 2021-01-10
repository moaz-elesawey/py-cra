# Python Create React App

**PyCRA** is a tool used to create a react frontend app for a backend server usually
**Flask** or **Django** backend.

the tool works a that, it creates a couple of dirs and files in a certain directory.
init a npm package.json in the directory. and with the babel it compile the react app into `static/js/main.py`.
and then it loaded into the `templates/*/index.html` then this html file is rendered by the **flask** or **django** backend server.

## Install
```sh
$ pip install py_cra
```

## Requirements
	- npm
	- nodejs
	- git
	- python>=3.6

## Usage
```sh
$ python -m PyCRA
```
#### Flask Usage
```sh
$ python -m PyCRA --mode=flask --app_dir=app
```
Here your have two options 
	- either you execute this command from outside your app directory like
		- ./
		- ../
		- app/
		- `$ python -m PyCRA --mode=flask --app_dir=app`
	- or fron inside your app directory like.
		- ./
		- ../
		- run.py
		- `$ python -m PyCRA --mode=flask --app_dir=.

replace the app with your application directory.

#### Django Usage
```sh
$ python -m PyCRA --mode=django --app_name=name
```
Here you must be in your `BASE_DIR` or the directory where the `manage.py` lives. this is important so your application did not get messed up.
**Make sure that you have create tha django app first before you execute the command.**

replace the name with your django app name

## Help
```
$ python -m PyCRA --help
usage: __main__.py [-h] [--mode MODE] [--app_name APP_NAME] [--app_dir APP_DIR]

optional arguments:
  -h, --help           show this help message and exit
  --mode MODE          django or flask mode
  --app_name APP_NAME  app name if django mode
  --app_dir APP_DIR    app dir if flask mode
```

## Post Creation

#### Django
In case of django backend add a view into the `frontend/views.py`.
In here we use the `frontend` name as the django app.
```python
from django.shortcuts import render

def index(request):
	return render(request=request, template_name='frontend/index.html')
```

#### Flask
In case of flask backend add a route to the `app.py`
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
```

## Info
please, make sure that this is only works a frontend app only.
so you cannot use something like **jinja templating** instead you should create a **rest api** as your backend server that can be created with eiher `flask_restful` in case of **Flask** or `django-restframework` in case of **Django**.


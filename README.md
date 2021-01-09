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
replace the app with your application directory.

#### Django Usage
```sh
$ python -m PyCRA --mode=django --app_name=name
```
replace the name with your django app name

## Help
```sh
$ python -m PyCRA --help
usage: __main__.py [-h] [--mode MODE] [--app_name APP_NAME] [--app_dir APP_DIR]

optional arguments:
  -h, --help           show this help message and exit
  --mode MODE          django or flask mode
  --app_name APP_NAME  app name if django mode
  --app_dir APP_DIR    app dir if flask mode
```


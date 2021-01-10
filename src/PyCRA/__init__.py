import os, json
from sys import argv
from pathlib import Path
from PyCRA.messages import COMMANDS_MESSAGES as CM
from PyCRA.files_content import (BABELRC_CONTENT,
                                WEBPACK_CONFIG_JS_CONTENT,
                                INDEX_JS_CONTENT,
                                INDEX_HTML_DJANGO_CONTENT,
                                INDEX_HTML_FLASK_CONTENT,
                                APP_JS_CONTENT)

__version__ = '0.0.3'

BASE_DIR = Path.cwd()


class PycraBase:


    def __init__(self, *args, **kwargs):

        # npm commands
        self._init_command = 'npm init -y'
        self._webpack_command = 'npm i webpack webpack-cli --save-dev'
        self._babel_command = 'npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev'
        self._react_command = 'npm i react react-dom --save-dev'

    def _create_file(self, content, filename):
        with open(filename, 'w') as f:
            f.write(content)

    def _execute_dirs_commands(self):
        print(CM.add_color(self._mk_components_dir))
        os.system(self._mk_components_dir)

        print(CM.add_color(self._mk_static_dir))
        os.system(self._mk_static_dir)

        print(CM.add_color(self._mk_templates_dir))
        os.system(self._mk_templates_dir)

    def _execute_npm_commands(self):
        ## execute npm commands
        print(CM.add_color(self._init_command))
        os.system(self._init_command)

        print(CM.add_color(self._webpack_command))
        os.system(self._webpack_command)

        print(CM.add_color(self._babel_command))
        os.system(self._babel_command)

        print(CM.add_color(self._react_command))
        os.system(self._react_command)

    def _add_run_scripts(self, inner_path):
        __package_file = f'{BASE_DIR}/{inner_path}/package.json'

        with open(__package_file) as inp:
            _data = json.loads(inp.read())
            _data['scripts'] = self._package_json_content
            inp.close()

            with open(__package_file, 'w') as out:
                out.write(json.dumps(_data, indent=4, sort_keys=False))


class PycraFlask(PycraBase):
    def __init__(self, app_dir, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app_dir = app_dir
        ## directories commands
        self._mk_components_dir = f'mkdir -p {BASE_DIR}/{self.app_dir}/src/components'
        self._mk_static_dir = f'mkdir -p {BASE_DIR}/{self.app_dir}/static/js'
        self._mk_templates_dir = f'mkdir -p {BASE_DIR}/{self.app_dir}/templates/'

        self._index_html_file = f'{BASE_DIR}/{self.app_dir}/templates/index.html'
        self._index_js_file = f'{BASE_DIR}/{self.app_dir}/src/index.js'
        self._babelrc_file = f'{BASE_DIR}/{self.app_dir}/.babelrc'
        self._webpack_config_js_file = f'{BASE_DIR}/{self.app_dir}/webpack.config.js'
        self._app_js_file = f'{BASE_DIR}/{self.app_dir}/src/components/App.js'

        '''we use a python dict here as we will use the json
            liberary to parse the package.json file first with the json.loads.
            and then modify the package.json "scritps" to our values "dev and build"
        '''
        self._package_json_content = {
                "dev": f"webpack --mode development --entry ./src/index.js --output-path ./static/js",
                "build": f"webpack --mode production --entry ./src/index.js --output-path ./static/js"
            }

    def execute(self):
        self._execute_dirs_commands()

        ## change dir into app_name
        print(CM.add_color(f'cd {BASE_DIR}/{self.app_dir}'))
        os.chdir(f'{BASE_DIR}/{self.app_dir}')

        ## execute npm commands
        self._execute_npm_commands()

        ## create npm files
        ## index.html
        print(CM.add_color(self._index_html_file, file_=True))
        self._create_file(INDEX_HTML_FLASK_CONTENT, self._index_html_file)

        ## webpack.config.js
        print(CM.add_color(self._webpack_config_js_file, file_=True))
        self._create_file(WEBPACK_CONFIG_JS_CONTENT, self._webpack_config_js_file)

        ## .babelrc
        print(CM.add_color(self._babelrc_file, file_=True))
        self._create_file(BABELRC_CONTENT, self._babelrc_file)

        ## index.js
        print(CM.add_color(self._index_js_file, file_=True))
        self._create_file(INDEX_JS_CONTENT, self._index_js_file)

        ## App.js
        print(CM.add_color(self._app_js_file, file_=True))
        self._create_file(APP_JS_CONTENT, self._app_js_file)

        ## change the package.json
        self._add_run_scripts(self.app_dir)


class PycraDjango(PycraBase):
    def __init__(self, app_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app_name = app_name

        ## directories commands
        if self.app_name is not None:
            self._mk_components_dir = f'mkdir -p {BASE_DIR}/{self.app_name}/src/components'
            self._mk_static_dir = f'mkdir -p {BASE_DIR}/{self.app_name}/static/{self.app_name}/js'
            self._mk_templates_dir = f'mkdir -p {BASE_DIR}/{self.app_name}/templates/{self.app_name}'

            self._index_js_file =  f'{BASE_DIR}/{self.app_name}/src/index.js'
            self._index_html_file = f'{BASE_DIR}/{self.app_name}/templates/{self.app_name}/index.html'
            self._webpack_config_js_file = f'{BASE_DIR}/{self.app_name}/webpack.config.js'
            self._babelrc_file = f'{BASE_DIR}/{self.app_name}/.babelrc'
            self._app_js_file = f'{BASE_DIR}/{self.app_name}/src/components/App.js'

            '''we use a python dict here as we will use the json
                liberary to parse the package.json file first with the json.loads.
                and then modify the package.json "scritps" to our values "dev and build"
            '''
            self._package_json_content = {
                    "dev": f"webpack --mode development --entry ./src/index.js --output-path ./static/{self.app_name}/js",
                    "build": f"webpack --mode production --entry ./src/index.js --output-path ./static/{self.app_name}/js"
                }
        else:
            raise ValueError('please include your app name')

    def execute(self):
        self._execute_dirs_commands()

        ## change dir into app_name
        os.chdir(f'{BASE_DIR}/{self.app_name}')

        ## execute npm commands
        self._execute_npm_commands()

        ## create npm files
        ## index.html
        print(CM.add_color(self._index_html_file, file_=True))
        self._create_file(INDEX_HTML_DJANGO_CONTENT.replace('{self.app_name}', self.app_name), self._index_html_file)

        ## webpack.config.js
        print(CM.add_color(self._webpack_config_js_file, file_=True))
        self._create_file(WEBPACK_CONFIG_JS_CONTENT, self._webpack_config_js_file)

        ## .babelrc
        print(CM.add_color(self._babelrc_file, file_=True))
        self._create_file(BABELRC_CONTENT, self._babelrc_file)

        ## index.js
        print(CM.add_color(self._index_js_file, file_=True))
        self._create_file(INDEX_JS_CONTENT, self._index_js_file)

        ## App.js
        print(CM.add_color(self._app_js_file, file_=True))
        self._create_file(APP_JS_CONTENT, self._app_js_file)

        ## change the package.json
        self._add_run_scripts(self.app_name)

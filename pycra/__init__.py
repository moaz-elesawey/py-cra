import os, json
from sys import argv
from pathlib import Path


BASE_DIR = Path.cwd()


class PycraBase:

    BABELRC_CONTENT = u'''{
    "presets": [
        "@babel/preset-env", "@babel/preset-react"
    ]
}'''

    WEBPACK_CONFIG_JS_CONTENT = u'''module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}'''

    INDEX_HTML_CONTENT = u'''<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Pycra Application</title>
    </head>
<body>
    <div id="app">
        <!-- React will load here -->
    </div>
</body>
    <!-- DJANGO_PLACEHOLDER -->
</html>'''

    APP_JS_CONTENT = '''import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <div>
        <h1 style={{textAlign: 'center'}}>Hello World</h1>
      </div>
    );
  }
}
export default App;

const container = document.getElementById("app");
render(<App />, container);'''

    INDEX_JS_CONTENT = u'''import App from "./components/App";'''


    def __init__(self, *args, **kwargs):

        # npm commands
        self._init_command = 'npm init -y'
        self._webpack_command = 'npm i webpack webpack-cli --save-dev'
        self._babel_command = 'npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev'
        self._react_command = 'npm i react react-dom --save-dev'

    def _create_file(self, content, filename):
        with open(filename, 'w') as f:
            f.write(content)

    def _execute_commands(self):
        os.system(self._mk_components_dir)
        os.system(self._mk_static_dir)
        os.system(self._mk_templates_dir)
        #os.system(self._cd_app_name)
        os.chdir(f'{BASE_DIR}/{self.app_name}')

        ## execute npm commands
        os.system(self._init_command)
        os.system(self._webpack_command)
        os.system(self._babel_command)
        os.system(self._react_command)

    def _add_run_scripts(self):
        __package_file = f'{BASE_DIR}/{self.app_name}/package.json'

        with open(__package_file) as inp:
            _data = json.loads(inp.read())
            _data['scripts'] = self._package_json_content
            inp.close()

            with open(__package_file, 'w') as out:
                out.write(json.dumps(_data, indent=4, sort_keys=False))


class PycraFlask(PycraBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass


class PycraDjango(PycraBase):
    def __init__(self, app_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app_name = app_name

        ## directories commands
        if self.app_name is not None:
            self._mk_components_dir = f'mkdir -p {BASE_DIR}/{self.app_name}/src/components'
            self._mk_static_dir = f'mkdir -p {BASE_DIR}/{self.app_name}/static/{self.app_name}'
            self._mk_templates_dir = f'mkdir -p {BASE_DIR}/{self.app_name}/templates/{self.app_name}'
            self._cd_app_name = f'cd {BASE_DIR}/{self.app_name}'

            '''we use a python dict here as we will use the json
                liberary to parse the package.json file first with the json.loads.
                and then modify the package.json "scritps" to our values "dev and build"
            '''
            self._package_json_content = {
                    "dev": f"webpack --mode development --entry ./src/index.js --output-path ./static/{self.app_name}",
                    "build": f"webpack --mode production --entry ./src/index.js --output-path ./static/{self.app_name}"
                }
        else:
            raise ValueError('please include your app name')

    def execute_commands(self):
        self._execute_commands()

        ## create npm files
        ## index.html
        self._create_file(self.INDEX_HTML_CONTENT, f'{BASE_DIR}/{self.app_name}/templates/{self.app_name}/index.html')

        ## webpack.config.js
        self._create_file(self.WEBPACK_CONFIG_JS_CONTENT, f'{BASE_DIR}/{self.app_name}/webpack.config.js')

        ## .babelrc
        self._create_file(self.BABELRC_CONTENT, f'{BASE_DIR}/{self.app_name}/.babelrc')

        ## index.js
        self._create_file(self.INDEX_JS_CONTENT, f'{BASE_DIR}/{self.app_name}/src/index.js')

        ## App.js
        self._create_file(self.APP_JS_CONTENT, f'{BASE_DIR}/{self.app_name}/src/components/App.js')

        ## change the package.json
        self._add_run_scripts()





















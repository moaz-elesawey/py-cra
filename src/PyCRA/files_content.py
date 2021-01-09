BABELRC_CONTENT = u'''{
    "presets": [
        "@babel/preset-env", "@babel/preset-react"
    ]
}'''

WEBPACK_CONFIG_JS_CONTENT = u'''module.exports = {
    watch: true,
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

INDEX_HTML_DJANGO_CONTENT = u'''<!DOCTYPE html>
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
    {% load static %}
    <script src="{% static '{self.app_name}/js/main.js' %}"></script>
</html>'''

INDEX_HTML_FLASK_CONTENT = u'''<!DOCTYPE html>
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
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
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



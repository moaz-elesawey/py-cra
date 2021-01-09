from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend/index.html')

if __name__ == '__main__':
    app.run(debug=True)

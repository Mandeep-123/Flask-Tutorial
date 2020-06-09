from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello connect check"


@app.route('/<name>')
def hello_name(name):
    return "Hello checked by {}!".format(name)

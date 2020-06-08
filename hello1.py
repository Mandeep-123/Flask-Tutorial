from flask import Flask
app = Flask(__name__)
@app.route('/') 
def index():
	return '<h1>Hello World!</h1>'


@app.route('/yep') 
def index1():
	return '<h1>Hello World!</h1>'

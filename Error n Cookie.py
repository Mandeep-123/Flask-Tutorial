from flask import Flask
from flask import make_response
app = Flask(__name__)
@app.route('/')
def index():
	return '<h1>Bad Request</h1>', 400

@app.route('/cooki')
def index1():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response

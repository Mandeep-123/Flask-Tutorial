from flask import request
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is {}</p>'.format(user_agent)
@app.route('/new')
def newfun():
	return '<a href="www.google.com">Google</a>'

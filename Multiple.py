from flask import Flask
from flask import redirect
from flask import abort
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello connect check"


@app.route('/<name>')
def hello_name(name):
    return "Hello checked by {}!".format(name)

@app.route('/redirect')
def redirecf():
	return redirect('http://www.google.com')

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, {}</h1>'.format(user.name)

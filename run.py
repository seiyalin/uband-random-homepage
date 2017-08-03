from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/')
def hello_seiya():
    return render_template('B17423.html')

@app.route('/A11167')
def hello_betty():
    return render_template('A11167.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
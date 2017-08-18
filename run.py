from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json_file(filepath):
	file = open(filepath,'r+', encoding='utf-8')
	file_text = json.load(file)
	return file_text

def get_userdata(file_text, student_number):
	userdata = {}
	for item in file_text:
		if item["student_number"] == student_number:
			userdata = item
			break;
	return userdata

@app.route('/')
def hello_world():
    file_text = read_json_file('static/data/index.json')
    return render_template('index.html', data=file_text)
  
@app.route('/<string:student_number>/details')
def details(student_number):
	#read json file
	file_text = read_json_file('static/data/index.json')
	userdata = get_userdata(file_text, student_number)
	return render_template('home.html', data=userdata)

@app.route('/<string:student_number>/eating')
def eating(student_number):
	#read json file
	file_text = read_json_file('static/data/index.json')
	userdata = get_userdata(file_text, student_number)
	return render_template('eating.html', data=userdata)

@app.route('/<string:student_number>/travelling')
def travelling(student_number):
	#read json file
	file_text = read_json_file('static/data/index.json')
	userdata = get_userdata(file_text, student_number)
	return render_template('travelling.html', data=userdata)

@app.route('/<string:student_number>/study')
def study(student_number):
	#read json file
	file_text = read_json_file('static/data/index.json')
	userdata = get_userdata(file_text, student_number)
	return render_template('study.html', data=userdata)

if __name__ == '__main__':
	app.debug = True
	app.run()
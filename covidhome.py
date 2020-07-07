from flask import Flask,render_template,request
from urllib.request import urlopen
import json

app = Flask(__name__)
app.secret_key = 'Abhi70#@'


@app.route('/')
def index():
	with urlopen('https://api.covid19api.com/summary') as res:
		# data = res.read()
		data = json.load(res)


	for key in data:
		value = data[key]
		# for key in value:
		# 	values = value[key]
		# 	return key
		# return value
	# return data
	return render_template('index.html', result=data)



if __name__ == "__main__":
	app.run(host="0.0.0.0")

from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():
	members = [
		{
			"name": "Alysson Alvaran", 
			"filename": "alysson.jpg"
		},
		{
			"name": "Paul Gilbert Arroyo", 
			"filename": "temp.png"
		},
		{
			"name": "Karl Andrew Gatdula", 
			"filename": "temp.png"
		},
		{
			"name": "Marc Derik Lopez", 
			"filename": "temp.png"
		},
		{
			"name": "Jose San Buenaventura", 
			"filename": "temp.png"
		}
	]
	filelocation = "/static/img/members/"

	return render_template('home.html', **locals())

@app.route("/demo/")
def demo():
	return render_template('demo.html')

@app.route('/api/get/', methods=['GET'])
def get():
	output = {
		"Status": "200"
	}
	
	return json.dumps(output)

@app.route('/api/post/', methods=['POST'])
def post():
	output = request.get_json()
	output["Status"] = "200"
	
	return json.dumps(output)
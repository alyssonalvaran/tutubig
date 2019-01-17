from flask import Flask, render_template, request, redirect, url_for
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
    return redirect(url_for('demo_dashboard'))

@app.route("/demo-dashboard/")
def demo_dashboard():
	return render_template('demo_dashboard.html')

@app.route("/demo-profile/")
def demo_profile():
	return render_template('demo.html')

@app.route("/demo-accounts/")
def demo_accounts():
	return render_template('demo.html')

@app.route("/demo-settings/")
def demo_settings():
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
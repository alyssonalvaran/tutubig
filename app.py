from flask import Flask, render_template, request

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

@app.route('/test/<user_input>', methods=['GET', 'POST'])
def test(user_input):
    output = 'test'
    if request.method == 'POST':
        output = 'POST'
    else:
        output = 'GET'
    return output + ': ' + user_input
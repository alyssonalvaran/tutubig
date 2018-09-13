from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/test/<user_input>', methods=['GET', 'POST'])
def test(user_input):
    output = 'test'
    if request.method == 'POST':
        output = 'POST'
    else:
        output = 'GET'
    return output + ': ' + user_input
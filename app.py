from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return render_template('welcome.html')

@app.route('/concept', methods=['GET'])
def concept():
    return render_template('concept.html')

@app.route('/merch', methods=['GET'])
def merch():
    return render_template('merch.html')

@app.route('/whoweare', methods=['GET'])
def whoweare():
    return render_template('whoweare.html')

@app.route('/guidelines', methods=['GET'])
def guidelines():
    return render_template('guidelines.html')

@app.route('/orders', methods=['GET'])
def orders():
    return render_template('orders.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
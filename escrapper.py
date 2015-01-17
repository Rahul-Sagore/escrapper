from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

with app.test_request_context():
	url_for('static', filename='skeleton.css')

if __name__ == '__main__':
	
    app.run(debug=True)

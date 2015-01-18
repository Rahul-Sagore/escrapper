# Importing flask, url_for - URL generation, render_template - Jinja template
from flask import Flask, url_for
from flask import render_template, flash, redirect
from forms import SearchForm
import scrapping

app = Flask(__name__)
app.config.from_object('config')

@app.route('/index/')
@app.route('/', methods=['GET', 'POST'])
def home():
	form = SearchForm()
	result = {}
	ptyp = ""
	#validating and processing form data
	if form.validate_on_submit():
		flash('Product  : %s' % (form.product_name.data))
		#tranferring input data to web scrapping script
		result = scrapping.scrap_input(form.product_name.data)
	
	return render_template('index.html', form=form, result=result)

with app.test_request_context():
	url_for('static', filename='skeleton.css')

if __name__ == '__main__':
    app.run(debug=True)

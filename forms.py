# importing form extension for flask
from flask.ext.wtf import Form
from wtforms import StringField #Importing form field class
from wtforms.validators import DataRequired #FOrm validation

class SearchForm(Form):
    product_name = StringField('product_name', validators=[DataRequired()])

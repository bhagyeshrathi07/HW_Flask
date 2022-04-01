from flask import flash, redirect, render_template, request
from app import myobj
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

class newForm(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@myobj.route("/", methods = ["GET", "POST"])
def home():
    form = newForm()
    if form.validate_on_submit ():
        flash(format(form.city.data))
        return redirect('/')
    return render_template('home.html', title = 'Home', name = name, city_names = city_names, form=form) 


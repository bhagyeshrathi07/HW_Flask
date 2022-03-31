from flask import flash, render_template, request
from app import myobj

@myobj.route("/", methods = ["GET", "POST"])
def home():
    name = 'Lisa'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    return render_template('home.html', title = 'Home', name = name, city_names = city_names, newCity = request.form.get("fname")) 


from flask import flash, message_flashed, redirect, render_template, request, url_for
from app import myapp

@myapp.route("/", methods = ["GET", "POST"])
def home():
    name = 'Lisa'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    return render_template('home.html', title = 'Home', name = name, city_names = city_names, newCity = request.form.get("fname")) 


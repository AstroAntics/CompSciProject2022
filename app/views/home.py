from flask import render_template, redirect, url_for
from app import app
from app.core.db.models import *


@app.route("/")
def index():
    return render_template("baseplate.html")


@app.route("/index")
def redirect_home():
    return redirect(url_for("index"))


@app.route("/allergens")
def show_allergens():
    return render_template("allergens.html", allergens=Allergen.query.all())


@app.route("/dishes")
def show_dishes():
    return render_template("dishes.html", dishes=Dish.query.all())


@app.route("/restaurants")
def show_restaurants():
    return render_template("restaurants.html", restaurants=Restaurant.query.all())


@app.route("/users")
def show_users():
    pass

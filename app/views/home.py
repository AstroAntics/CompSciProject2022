from flask import render_template, redirect, url_for, request, abort
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


@app.route("/allergens/new", methods=['GET', 'POST'])
def new_allergen():
    if request.method == 'POST':
        allergen_title = request.form['allergenTitle']
        allergen_desc = request.form['allergenDesc']
        # allergen_dangerous = request.form['isDangerous']
        # prevent duplicate allergen titles
        if Allergen.query.filter_by(title=allergen_title).first():
            # duplicate title exists, and we can't allow that
            return render_template("new_allergen.html", error="Duplicate of existing dish.")
        else:
            # no duplicates, good to go
            allergen = Allergen(
                title=allergen_title,
                description=allergen_desc,
                # is_dangerous=allergen_dangerous
            )
            db.session.add(allergen)
            db.session.commit() # save to db
            return redirect("/allergens")
    return render_template("new_allergen.html")


@app.route("/dishes")
def show_dishes():
    return render_template("dishes.html", dishes=Dish.query.all())


@app.route("/dishes/new", methods=['GET', 'POST'])
def new_dish():
    if request.method == 'POST':
        dish_title = request.form['dishTitle']
        dish_desc = request.form['dishDesc']
        # prevent duplicate dish titles
        if Dish.query.filter_by(title=dish_title).first():
            # duplicate title exists, and we can't allow that
            return render_template("new_dish.html", error="Duplicate of existing dish.")
        else:
            # no duplicates, good to go
            dish = Dish(title=dish_title, description=dish_desc)
            db.session.add(dish)
            db.session.commit() # save dish to db
            return redirect("/dishes")
    return render_template("new_dish.html")


@app.route("/dishes/delete/<dish>", methods=['POST']) # do not allow get requests for deletion
def delete_dish(dish):
    if request.method == 'POST':
        db.session.delete(dish)
        db.session.commit()
        # also, before we delete the dish, let's make sure it's _actually_ deleted
        # and we sort by id instead of title here
        if Dish.query.filter_by(title=dish.id).first():
            # still exists, abort
            # this should never happen
            return render_template("delete_dish.html")
        else:
            return redirect("/dishes")


@app.route("/restaurants")
def show_restaurants():
    return render_template("restaurants.html", restaurants=Restaurant.query.all())


@app.route("/restaurants/new", methods=['GET', 'POST'])
def new_restaurant():
    if request.method == 'POST':
        restaurant_title = request.form['restaurantTitle']
        restaurant_desc = request.form['restaurantDesc']
        # prevent duplicate restaurant titles
        if Restaurant.query.filter_by(title=restaurant_title).first():
            # duplicate title exists, and we can't allow that
            return render_template("new_restaurant.html", error="Duplicate of existing dish.")
        else:
            # no duplicates, good to go
            restaurant = Restaurant(
                title=restaurant_title,
                description=restaurant_desc
            )
            db.session.add(restaurant)
            db.session.commit()  # save to db
            return redirect("/restaurants")
    return render_template("new_restaurant.html")


@app.route("/users")
def show_users():
    pass # noop


@app.route("/about")
def about_us():
    return "<p>This page is a work in progress. Come back later.</p>"

import os
from flask import render_template, redirect, url_for, request, abort
from flask import send_from_directory # second line of Flask imports
from app import app
from app.core.db.models import *


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/index")
def redirect_home():
    return redirect(url_for("index"))


@app.route('/favicon.ico')
# Courtesy of <https://thewebdev.info/2020/10/08/python-web-development-with-flask>
def favicon():
    return send_from_directory(
        os.path.join(
            app.root_path, 'static'
        ), 'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )


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


@app.route("/allergens/delete/<id>", methods=['GET', 'POST']) # do not allow get requests for deletion
def delete_allergen(allergen):
    if request.method == 'POST':
        db.session.delete(allergen)
        db.session.commit()
        return render_template("allergens.html")


@app.route("/dishes")
def show_dishes():
    return render_template("dishes.html", dishes=Dish.query.all())


@app.route("/dishes/<int:_id>")
def show_specific_dish(_id):
    # show specific dish as opposed to all of them
    dish = Dish.query.filter_by(id=_id).first()
    if dish:
        return render_template("view_dish.html", dish=dish)
    else:
        abort(404)


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


@app.route("/dishes/delete/<int:_id>", methods=['GET', 'POST'])
def delete_dish(_id):
    _dish = Dish.query.filter_by(id=_id).first()
    if request.method == 'POST':
        # do not allow get delete requests
        if _dish:
            db.session.delete(_dish)
            db.session.commit()
            return redirect("dishes.html")
        return render_template("delete_dish.html", dish=_dish)


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


@app.route("/restaurants/delete/<id>", methods=['GET', 'POST']) # do not allow get requests for deletion
def delete_restaurant(restaurant):
    if request.method == 'POST':
        db.session.delete(restaurant)
        db.session.commit()
        return render_template("dishes.html")


@app.route("/users")
def show_users():
    pass # noop


@app.route("/about")
def about_us():
    return "<p>This page is a work in progress. Come back later.</p>"

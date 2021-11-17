from flask import render_template, redirect, url_for
from app import app


@app.route("/")
def index():
    return render_template("baseplate.html")


@app.route("/index")
def redirect_home():
    return redirect(url_for("index"))

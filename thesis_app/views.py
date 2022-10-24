from flask import Flask, render_template
from . import app


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("construction.html")

@app.route("/proposal/")
def proposal():
    return render_template("proposal.html")

@app.route("/teams/")
def teams():
    return render_template("construction.html")

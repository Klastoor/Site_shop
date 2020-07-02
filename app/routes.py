from flask import render_template, redirect, request, url_for
from app import app

@app.route("/")
@app.route("/base.html")
def base():
    return render_template("base.html")
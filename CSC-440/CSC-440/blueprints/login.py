from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)

loginBP = Blueprint('login', __name__)

@loginBP.route("/login")
def login():
	return render_template('login/login.html')

@loginBP.route("/register")
def register():
	return render_template('login/register.html')
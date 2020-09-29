from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)

viewBP = Blueprint('view', __name__)

@viewBP.route("/view")
def view():
	return render_template('view/view.html')
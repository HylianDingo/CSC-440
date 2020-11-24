from flask import (
    Blueprint, flash, g, request, redirect, render_template, request, session, url_for, make_response
)
from werkzeug.utils import secure_filename
from flask import current_app as app
import os

viewBP = Blueprint('view', __name__)

@viewBP.route("/view", methods=['GET', 'POST'])
def view():
	path = os.getcwd()+"\\CSC-440\\static\\files"
	filesList = []

	for file in os.listdir(path):
		filesList.append(file)

	if request.method == 'POST':
		if request.form.get('current-file'):
			selectedFile = request.form.get('current-file')

			openFile = []
			baseFile = open('CSC-440/static/files/' + selectedFile, 'r').readlines()
			for line in baseFile:
				openFile.append(line)

			return render_template('view/view.html', filesList=filesList, openFile=openFile)
		
	return render_template('view/view.html', filesList=filesList)

@viewBP.route("/upload", methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		filename = secure_filename(file.filename)
		if fileAllowed(filename):
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return uploadStatus(True)
		else:
			return uploadStatus(False)

	return render_template('view/upload.html')

@viewBP.route("/success")
def uploadStatus(uploaded):
	if uploaded:
		alert = 'upload successful!'
		return render_template("view/view.html", message=alert)
	else:
		alert  = 'upload failed.\\nplease ensure the file is of type csv.'
		return render_template("view/view.html", message=alert)


def fileAllowed(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

import os
from flask import Flask
from .blueprints.view import viewBP
from .blueprints.login import loginBP



def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)

	app.register_blueprint(viewBP)
	app.register_blueprint(loginBP)


	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)

	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# a simple page that says hello
	@app.route('/')
	def hello():
		return 'Index'

	return app

def main():
	app = create_app()
	app.run(debug=True, host='0.0.0.0', port=5000)
	print(app.static_folder)
	print(app.template_folder)

# only occurs when running the script directly (local)
if __name__ == '__main__':
	main()
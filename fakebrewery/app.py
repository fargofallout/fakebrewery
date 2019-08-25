import flask
import sys
import os

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, folder)
# os.environ["FLASK_APP"] = "fakebrewery"
# os.environ["FLASK_ENV"] = "development"
# print(f"folder: {folder}")
# print(f"folder2: {folder2}")
# print(f"sys.path: {sys.path}")
# print(f"environ: {os.environ}")

import fakebrewery.db.db_utils as db_utils


app = flask.Flask(__name__, instance_relative_config=True)

def main():
	register_blueprints()
	setup_db()
	app.run(debug=True)

def setup_db():
	db_path = "whatever"
	db_utils.db_init(db_path)

def register_blueprints():
	from fakebrewery.views import home
	app.register_blueprint(home.bp)

	from fakebrewery.views import beers
	app.register_blueprint(beers.bp)

	from fakebrewery.views import about
	app.register_blueprint(about.bp)

	from fakebrewery.views import faq
	app.register_blueprint(faq.bp)

if __name__ == "__main__":
	main()


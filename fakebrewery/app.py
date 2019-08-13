import flask

app = flask.Flask(__name__)

def main():
	register_blueprints()
	app.run(debug=True)

def register_blueprints():
	from views import home
	app.register_blueprint(home.bp)

	from views import beers
	app.register_blueprint(beers.bp)

if __name__ == "__main__":
	main()


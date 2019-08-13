import flask

bp = flask.Blueprint("beers", __name__, template_folder="templates")

@bp.route("/beers/")
def beers():
	return flask.render_template("beers/beers.html")

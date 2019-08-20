import flask

bp = flask.Blueprint("about", __name__, template_folder="templates")

@bp.route("/about/")
def about():
	return flask.render_template("about/about.html")

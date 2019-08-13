import flask

bp = flask.Blueprint("home", __name__, template_folder="templates")

@bp.route("/home/")
@bp.route("/")
def home():
	return flask.render_template("home/home.html")

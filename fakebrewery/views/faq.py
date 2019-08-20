import flask

bp = flask.Blueprint("faq", __name__, template_folder="templates")

@bp.route("/faq/")
def faq():
	return flask.render_template("faq/faq.html")

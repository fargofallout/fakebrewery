import flask

from fakebrewery.db.beer import Beer
from fakebrewery.db.style import Style
import fakebrewery.db.db_utils as db_utils

import time

bp = flask.Blueprint("home", __name__, template_folder="templates")

@bp.route("/home/")
@bp.route("/")
def home():
	start_time = time.time()
	a_style = Style(style_name="Stout",
					glass_type="stout glass?",
					style_description="tasty")
	with db_utils.modify_session() as db_session:
		db_session.add(a_style)
	print(f"took {time.time() - start_time} seconds to add the style")

	start_time = time.time()
	with db_utils.query_session() as db_session:
		the_style = db_session.query(Style).filter(Style.style_name=="Stout").first()
	print(f"took {time.time() - start_time} seconds to query the style")

	print(f"style type: {the_style}")
	start_time = time.time()
	a_beer = Beer(beer_name="Mornin' Delight",
					beer_style=the_style.id,
					abv="10.0",
					ibu="40?",
					beer_description="It's a stout, silly. Tasty!",
					beer_on_tap=True)

	with db_utils.modify_session() as db_session:
		db_session.add(a_beer)
	print(f"took {time.time() - start_time} seconds to add the beer")

	with db_utils.query_session() as db_session:
		a_beer = db_session.query(Beer).filter(Beer.beer_name=="Mornin' Delight").first()

	print("testing how often I'm hitting the database")
	print(f"beer name: {a_beer.beer_name}")
	print(f"beer style: {a_beer.style_rel.style_name}")

	return flask.render_template("home/home.html")

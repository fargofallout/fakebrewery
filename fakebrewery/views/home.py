import flask
import time

from fakebrewery.db.beer import Beer
from fakebrewery.db.style import Style
from fakebrewery.db.glass import Glass
import fakebrewery.db.db_utils as db_utils

bp = flask.Blueprint("home", __name__, template_folder="templates")

@bp.route("/home/")
@bp.route("/")
def home():

	# add dummy data to db
	# file_in = open("views\\dummy_data.txt", "r", encoding="utf-8")
	# for line in file_in:
	# 	temp_line = line.rstrip("\n").split("\t")
	# 	if temp_line[0] == "glass":
	# 		print("hitting glass type, right?")
	# 		with db_utils.modify_session() as db_session:
	# 			db_session.add(Glass(glass_name=temp_line[1], glass_description=temp_line[2]))

	# 	elif temp_line[0] == "style":
	# 		print("am I hitting this?")
	# 		with db_utils.query_session() as db_session:
	# 			the_glass = db_session.query(Glass).filter(Glass.glass_name==temp_line[2]).first()
	# 		with db_utils.modify_session() as db_session:
	# 			db_session.add(Style(style_name=temp_line[1],
	# 									style_glass=the_glass.id,
	# 									style_description=temp_line[3]))

	# 	elif temp_line[0] == "beer":
	# 		print("getting to beers")
	# 		beer_on_tap = False
	# 		beer_in_growlers = False
	# 		beer_in_bottles = False
	# 		if temp_line[5].lower() == "true":
	# 			beer_on_tap = True
	# 		if temp_line[6].lower() == "true":
	# 			beer_in_growlers = True
	# 		if temp_line[7].lower() == "true":
	# 			beer_in_bottles = True

	# 		with db_utils.query_session() as db_session:
	# 			the_style = db_session.query(Style).filter(Style.style_name==temp_line[8]).first()

	# 		with db_utils.modify_session() as db_session:
	# 			db_session.add(Beer(beer_name=temp_line[1],
	# 									abv=temp_line[2],
	# 									ibu=temp_line[3],
	# 									beer_description=temp_line[4],
	# 									beer_on_tap=beer_on_tap,
	# 									beer_in_growlers=beer_in_growlers,
	# 									beer_in_bottles=beer_in_bottles,
	# 									beer_style=the_style.id))

	# file_in.close()


	with db_utils.query_session() as db_session:
		a_beer = db_session.query(Beer).filter(Beer.beer_name=="Mornin' Delight").first()

	print("testing how often I'm hitting the database")
	print(f"beer name: {a_beer.beer_name}")
	print(f"beer style: {a_beer.style_rel.style_name}")
	print(f"glass to use? {a_beer.style_rel.glass_rel.glass_name}")

	return flask.render_template("home/home.html")

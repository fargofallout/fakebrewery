import sqlalchemy as sa
import sqlalchemy.orm as orm
from fakebrewery.db.base import Base

class Beer(Base):
	__tablename__ = "beers"
	id = sa.Column(sa.Integer, primary_key=True)
	beer_name = sa.Column(sa.String)
	beer_style = sa.Column(sa.Integer, sa.ForeignKey("styles.id"))
	style_rel = orm.relationship("Style", back_populates="beer_rel", lazy="joined")
	abv = sa.Column(sa.String) # not sure if this should be a float
	ibu = sa.Column(sa.String) # float here, too?
	# beer_glass = sa.Column(sa.Integer, sa.ForeignKey("glasses.id"))
	# glass_rel = orm.relationship("Glass", back_populates="beer_rel")
	beer_description = sa.Column(sa.String)
	beer_on_tap = sa.Column(sa.Boolean)
	beer_in_crowlers = sa.Column(sa.Boolean)
	beer_in_bottles = sa.Column(sa.Boolean)


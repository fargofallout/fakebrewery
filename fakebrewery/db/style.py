import sqlalchemy as sa
import sqlalchemy.orm as orm
from fakebrewery.db.base import Base

class Style(Base):
	__tablename__ = "styles"
	id = sa.Column(sa.Integer, primary_key=True)
	style_name = sa.Column(sa.String)
	glass_type = sa.Column(sa.String)
	style_description = sa.Column(sa.String)

	beer_rel = orm.relationship("Beer", back_populates="style_rel", lazy="joined")

	print("***\n***\ndo I create an object???\n***\n***")


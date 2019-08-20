import sqlalchemy as sa
import sqlalchemy.orm as orm
from fakebrewery.db.base import Base

class Style(Base):
	__tablename__ = "styles"
	id = sa.Column(sa.Integer, primary_key=True)
	style_name = sa.Column(sa.String)
	style_description = sa.Column(sa.String)

	style_glass = sa.Column(sa.Integer, sa.ForeignKey("glasses.id"))
	glass_rel = orm.relationship("Glass", back_populates="beer_rel", lazy="joined")
	beer_rel = orm.relationship("Beer", back_populates="style_rel", lazy="joined")


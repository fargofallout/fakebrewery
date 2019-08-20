import sqlalchemy as sa
import sqlalchemy.orm as orm
from fakebrewery.db.base import Base

class Glass(Base):
	__tablename__ = "glasses"
	id = sa.Column(sa.Integer, primary_key=True)
	glass_name = sa.Column(sa.String)
	glass_description = sa.Column(sa.String)

	beer_rel = orm.relationship("Style", back_populates="glass_rel", lazy="joined")
	

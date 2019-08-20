import sqlalchemy as sa
import sqlalchemy.orm as orm
from contextlib import contextmanager

from fakebrewery.db.base import Base

Session = None

def db_init(db_path):
	# 
	global Session

	if Session:
		return

	engine = sa.create_engine("sqlite:///db/brewerydata.db", echo=True)
	Session = orm.sessionmaker(bind=engine)
	import fakebrewery.db.__all_db_classes
	Base.metadata.create_all(engine)

@contextmanager
def query_session():
	global Session
	db_session = Session()
	try:
		yield db_session
	except:
		raise
	finally:
		db_session.close()

@contextmanager
def modify_session():
	global Session
	db_session = Session()
	try:
		yield db_session
		db_session.commit()
	except:
		raise
	finally:
		db_session.close()


from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


url = "sqlite:///apidb.sqlite"


engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()




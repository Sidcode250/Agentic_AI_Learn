from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:sid1653@localhost:5432/Trial1"

engine = create_engine(db_url)
 
session = sessionmaker(autocommit=False, autoflush=False,bind=engine)
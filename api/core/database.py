from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:akram7282@localhost:3306/fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 

class Base(DeclarativeBase):
  pass

def get_db():
  db = sessionLocal()
  try: 
    yield db
  finally:
    db.close()
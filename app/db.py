from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base 

SQLALCHEMY_DATABASE_URL="postgresql://postgres:meryem%40@localhost:5432/optic_manager_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind=engine)

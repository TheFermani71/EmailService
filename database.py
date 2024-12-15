from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for models
Base = declarative_base()

# Database URL
DATABASE_URL = "sqlite:///subscribers.db"

# Create engine and session factory
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

def init_db():
    """
    Initialize the database and create tables if they don't exist.
    """
    Base.metadata.create_all(engine)
    print("Database initialized.")

def get_session():
    """
    Get a new database session.
    """
    return Session()

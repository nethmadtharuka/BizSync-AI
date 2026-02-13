from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# Create database engine (connection pool)
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Create session factory (sessions = temporary database connections)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all database models
class Base(DeclarativeBase):
    pass

# Dependency function - opens DB connection, does work, closes it
def get_db():
    db = SessionLocal()
    try:
        yield db  # Give the connection to the API route
    finally:
        db.close()  # Always close when done
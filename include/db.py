from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

load_dotenv("env.dev")

# postgres_pw = os.getenv("POSTGRES_PASSWORD")
# postgres_user =  os.getenv("POSTGRES_USER")
# postgres_db = os.getenv("POSTGRES_DB")
# postgres_host = os.getenv("DB_HOST")
# postgres_port = os.getenv("POSTGRES_PORT")


def construct_database_url():
    """
    Construct the database URL from the environment variables.
    Returns:
    - database_url: `sqlalchemy.engine.url.URL` - The database URL.

    """
    return URL.create(
        drivername="postgresql",
        username=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )

SQLALCHEMY_DATABASE_URL = construct_database_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
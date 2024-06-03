import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alembic.config import Config

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("SA_PASSWORD")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_driver = os.getenv("DB_DRIVER")
DATABASE_URL = f"mssql+pyodbc://{username}:{password}@localhost:{db_port}/{db_name}?driver={db_driver}&TrustServerCertificate=yes"

# Create the sql alchemy datase engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the alembic config object
config = Config()
config.set_main_option("sqlalchemy.url", DATABASE_URL)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

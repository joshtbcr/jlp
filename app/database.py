import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}/{settings.DB_NAME}"

# Retry mechanism for database connection
max_retries = 5
retry_delay = 3  # seconds

for attempt in range(max_retries):
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        if not database_exists(engine.url):
            create_database(engine.url)
        break
    except Exception as e:
        print(f"Database connection failed (attempt {attempt + 1}/{max_retries}): {e}")
        if attempt < max_retries - 1:
            time.sleep(retry_delay)
        else:
            raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

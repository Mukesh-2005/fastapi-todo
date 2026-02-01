from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker, declarative_base;
from dotenv import load_dotenv;
import os;
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set.")

# Normalize scheme: SQLAlchemy expects 'postgresql' (not 'postgres')
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
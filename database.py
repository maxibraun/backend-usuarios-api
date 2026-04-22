import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL") # or "sqlite:///local.db"
#print(DATABASE_URL)

Base = declarative_base()

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg2://", 1)
    
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
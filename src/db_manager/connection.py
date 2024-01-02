from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_manager.config import DATABASE


engine = create_engine(DATABASE, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
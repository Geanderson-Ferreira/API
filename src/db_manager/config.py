import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

DATABASE = os.getenv('DATABASE')
DB_NAME = os.getenv('DB_NAME')
MY_IP = os.getenv('MY_IP')
API_PREFIX = '/api'
ENGINE = create_engine(DATABASE, pool_pre_ping=True)
SESSION = sessionmaker(bind=ENGINE)
BASE = declarative_base()
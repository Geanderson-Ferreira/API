import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv('DATABASE') #'sqlite:///example.db'
DB_NAME = os.getenv('DB_NAME') #'example.db'
MY_IP = os.getenv('MY_IP') #'10.0.0.102'
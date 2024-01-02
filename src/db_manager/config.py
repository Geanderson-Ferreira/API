import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv('DATABASE')
DB_NAME = os.getenv('DB_NAME')
MY_IP = os.getenv('MY_IP')
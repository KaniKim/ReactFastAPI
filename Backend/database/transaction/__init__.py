import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
database = os.environ.get("DB_NAME")
port = os.environ.get("DB_PORT")

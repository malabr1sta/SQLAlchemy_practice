from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.environ.get('DATABASE_NAME')
DB_HOST = os.environ.get('DATABASE_HOST')
DB_PORT = os.environ.get('DATABASE_PORT')
DB_USER = os.environ.get('DATABASE_USER')
DB_PASS = os.environ.get('DATABASE_PASSWORD')

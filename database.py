import mysql.connector as connection
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection(db_name):
    return connection.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=db_name
    )
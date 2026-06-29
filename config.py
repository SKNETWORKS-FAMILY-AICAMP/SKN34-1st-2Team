import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY") if os.getenv("API_KEY") else "d3c50f72560e702df41c006c8dbf049cf4e8fd3c415f0ed01fb3352ac010ddc8"
DB_HOST = os.getenv("DB_HOST") if os.getenv("DB_HOST") else "localhost"
DB_USER = os.getenv("DB_USER") if os.getenv("DB_USER") else "root"
DB_PASSWORD = os.getenv("DB_PASSWORD") if os.getenv("DB_PASSWORD") else "1234"
DB_NAME = os.getenv("DB_NAME") if os.getenv("DB_NAME") else "test"
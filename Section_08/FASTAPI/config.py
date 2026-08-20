import os
import json

from dotenv import load_dotenv

load_dotenv()

class Settings:
    origins = json.loads(os.getenv("ORIGINS", "[]"))    #os.getenv() environment variable ko string ke form me return karta hai, Python list nahi.
    SECRET_KEY = os.getenv("SECRET_KEY")
    DB_URL = os.getenv("DB_URL")

settings = Settings()
from dotenv import load_dotenv
import os

load_dotenv()

print("DB_NAME from env:", os.getenv("DB_NAME"))

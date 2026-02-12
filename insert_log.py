import os 
import datetime
import mysql.connector
from dotenv import load_dotenv 


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASSWORD,
    database = DB_NAME,
)

log_scrtime = float(input("Enter screen time (hours) : \n"))
log_sleep = float(input("Enter Total sleep hours : \n"))
log_study = float(input("Enter Total study hours : \n"))

log_date = datetime.date.today()

cursor = conn.cursor()
query = "INSERT INTO daily_log (log_scrtime,log_sleep,log_study,log_date) VALUES(%s,%s,%s,%s)"
values = (log_scrtime, log_sleep ,log_study ,log_date)  

cursor.execute(query,values)
cursor.close()
conn.commit()
conn.close()
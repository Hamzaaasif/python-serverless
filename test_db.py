#!/usr/bin/python3
import os
import pymysql

# Database connection parameters - update as needed
DB_USER=os.getenv('DB_USER') or 'root'
DB_PSWD=os.getenv('DB_PSWD') or 'root'
DB_HOST=os.getenv('DB_HOST') or '34.133.103.199'
DB_NAME=os.getenv('DB_NAME') or 'task_logger'
DB_PORT=os.getenv('DB_PORT') or 3307

db = pymysql.connect(host=DB_HOST,
										 user=DB_USER, 
										 password=DB_PSWD, 
										 database=DB_NAME, 
										 cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
cursor.execute("SHOW DATABASES")

print("Content-type: text/html\n")
print("Setup Successful")

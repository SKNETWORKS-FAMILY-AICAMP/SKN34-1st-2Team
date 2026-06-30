import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)


# import mysql.connector
# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Database:
#     def __init__(self):
#         self.conn = self.connect()

#     def connect(self):
#         try:
#             connection = mysql.connector.connect(
#                 host = os.getenv("DB_HOST"),
#                 user = os.getenv("DB_USER"),
#                 password = os.getenv("DB_PASSWORD"),
#                 database = os.getenv("DB_NAME")
#             ) 
#             if connection.is_connected():
#                 print('db연결성공') # 추후삭제
#                 return connection
#         except mysql.connector.Error as err:
#             print(f"DB 연결 실패: {err}")
#             return None
#     def close(self):
#         if self.conn and self.conn.is_connected():
#             self.conn.close()

# db = Database()

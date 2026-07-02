import mysql.connector
import config as cf

class Database:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host = cf.DB_HOST,
                user = cf.DB_USER,
                password = cf.DB_PASSWORD,
                database = cf.DB_NAME
            ) 
            if connection.is_connected():
                # print('db연결성공') # 추후삭제
                return connection
            
        except mysql.connector.Error as err:
            print(f"DB 연결 실패: {err}")
            return None
        
    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            
    # crud 함수
    def execute(self, sql, params=None):
        try:
            if not self.conn or not self.conn.is_connected():
                self.conn = self.connect()

            with self.conn.cursor(dictionary=True) as cursor: 
                # 값이 있으면 값을 넣고 없으면 튜플
                cursor.execute(sql, params or ())
                
                # select 인지 검사
                if sql.strip().lower().startswith("select"):
                    return cursor.fetchall()

                self.conn.commit()
                return cursor.rowcount

        except mysql.connector.Error as err:
            print("SQL ERROR:", err)
            return None

db = Database()
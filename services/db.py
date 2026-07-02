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
                print('db연결성공') # 추후삭제
                return connection
            
        except mysql.connector.Error as err:
            print(f"DB 연결 실패: {err}")
            return None
        
    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            
    def execute(self, sql, params=None):
        """
        SELECT / INSERT / UPDATE / DELETE 모두 처리
        SELECT면 list 반환
        나머지는 rowcount 반환
        """

        try:
            # connection 체크 (Streamlit 대비)
            if not self.conn or not self.conn.is_connected():
                self.conn = self.connect()

            cursor = self.conn.cursor(dictionary=True)

            cursor.execute(sql, params or ())

            # SELECT
            if sql.strip().lower().startswith("select"):
                result = cursor.fetchall()
            else:
                self.conn.commit()
                result = cursor.rowcount

            cursor.close()
            return result

        except mysql.connector.Error as err:
            print(f"SQL 실행 실패: {err}")
            return None

db = Database()
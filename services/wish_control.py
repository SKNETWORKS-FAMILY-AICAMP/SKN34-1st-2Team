import mysql.connector
from services.db import db

# wishlist에 주유소/주차장이 있는지 확인 함수
def is_wish(type, name, addr):
    if db.conn and db.conn.is_connected():
        cursor = db.conn.cursor()
        # 들어온 주유수/주차장 wishlist 테이블에 조회
        sql = 'SELECT wish_id FROM wishlist WHERE type=%s AND name=%s AND addr=%s'
        values = (type, name, addr)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        # 주유소/주차장이 있다면 True, 없다면 False
        return bool(result)
    return False

# wishlist에 추가 or 삭제 함수
def toggle_wish(type, name, addr, phone, is_wish):
    if db.conn and db.conn.is_connected():
        cursor = db.conn.cursor()
        # wishlist 테이블에 있다면 삭제
        if is_wish:
            sql = 'DELETE FROM wishlist WHERE type=%s AND name=%s AND addr=%s'
            values = (type, name, addr)
            cursor.execute(sql, values)
        # wishlist 테이블에 없다면 추가
        else:
            sql = 'INSERT INTO wishlist (type, name, addr, phone) VALUES (%s, %s, %s, %s)'
            values = (type, name, addr, phone)

        db.conn.commit()
        cursor.close()
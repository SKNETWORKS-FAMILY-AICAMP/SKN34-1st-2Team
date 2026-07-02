import mysql.connector
from services.db import db

# wishlist에 주유소/주차장이 있는지 확인 함수
def is_wish(type, name, addr):
    
    # 들어온 주유소/주차장 wishlist 테이블에 조회
    sql = 'SELECT wish_id FROM wishlist WHERE type=%s AND name=%s AND addr=%s'
    values = (type, name, addr)
    result = db.execute(sql, values)
    # 주유소/주차장이 있다면 True, 없다면 False
    return bool(result)

# wishlist에 추가 or 삭제 함수
def toggle_wish(type, name, addr, phone, is_wish):
    # wishlist 테이블에 있다면 삭제
    if is_wish:
        sql = 'DELETE FROM wishlist WHERE type=%s AND name=%s AND addr=%s'
        values = (type, name, addr)
        db.execute(sql, values)
    # wishlist 테이블에 없다면 추가
    else:
        sql = 'INSERT INTO wishlist (type, name, addr, phone) VALUES (%s, %s, %s, %s)'
        values = (type, name, addr, phone)
        db.execute(sql, values)

# wishlist 테이블 데이터 반환 함수
def get_wish(type, key=None):
    # 리턴할 리스트 선언
    data_wish = []

    # 내 주유소/주차장 조회 및 data_wish에 할당
    if key:
        sql = 'SELECT name, addr, phone FROM wishlist WHERE type = %s and addr LIKE %s ORDER BY created_at DESC'
        data_wish = db.execute(sql, (type, f'%{key}%'))
    else:
        sql = 'SELECT name, addr, phone FROM wishlist WHERE type = %s ORDER BY created_at DESC'
        data_wish = db.execute(sql, (type, ))
    
    return data_wish

# good_oil 테이블 데이터 반환 함수
def get_good_oil(key=None):
    # 리턴할 리스트 선언
    data_good= []

    # 착한 주유소 조회 및 data_good에 할당
    if key:
        sql = 'SELECT g_name, g_addr, g_phone, gasoline_price, diesel_price FROM goodoil WHERE g_addr LIKE %s'
        data_good = db.execute(sql, (f'%{key}%', ))
    else:
        sql = 'SELECT g_name, g_addr, g_phone, gasoline_price, diesel_price FROM goodoil'
        data_good = db.execute(sql)
        
    return data_good

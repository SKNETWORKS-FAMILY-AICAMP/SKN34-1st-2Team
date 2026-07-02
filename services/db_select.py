from db import Database

# 착한 주유소 위도 경도 (전화번호 컬럼 기준 조인)
def goodoil_loc():
    db = Database()
    if not db.conn:
        return
    
    cursor = db.conn.cursor(dictionary=True) # 딕셔너리 형태로 반환

    sql = """
        SELECT 
            g.g_name, 
            g.g_addr, 
            g.g_phone, 
            g.gasoline_price, 
            g.diesel_price, 
            o.latitude, 
            o.longitude
        FROM goodoil g
        JOIN oil o
        ON g.g_phone = o.o_phone
    """

    try: 
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        print(f"조회 오류 : {e}")
        return []
    
    finally:
        cursor.close()
        db.close()
import csv
from db import Database

db = Database()

# 주차장 데이터 삽입
if db.conn:
    cursor = db.conn.cursor()

    try:
        with open("data/parkinglots_data.csv", "r", encoding = 'cp949') as csvfile:
            reader = csv.DictReader(csvfile)

            insert_count = 0
            for row in reader:
                p_name = row.get('주차장명')
                p_addr = row.get('소재지지번주소')
                p_phone = row.get('전화번호')
                latitude = row.get('위도')
                longitude = row.get('경도')

                if not p_name:  # 주차장명이 null이면 넘어감
                    continue
                
                if not latitude or not longitude:
                    continue

                sql = """
                    INSERT INTO park (p_name, p_addr, p_phone, latitude, longitude)
                    VALUES (%s, %s, %s, %s, %s)
                """

                cursor.execute(sql, (p_name, p_addr, p_phone, latitude, longitude))
                insert_count += 1

            db.conn.commit()
            print(f'주차장 데이터 {insert_count}건 저장 완')

    except FileNotFoundError:
        print("CSV 파일을 찾을 수 없음")
    except Exception as e:
        print(f"오류 발생: {e}")
        db.conn.rollback()  # 에러 나면 되돌리기 

    finally:
        cursor.close()


# 주유소 데이터 삽입
if db.conn:
    cursor = db.conn.cursor()

    try:
        with open("data/gasstation_data.csv", "r", encoding = 'cp949') as csvfile:
            reader = csv.DictReader(csvfile)

            insert_count = 0
            for row in reader:
                o_name = row.get('주유소명')
                o_addr = row.get('소재지지번주소')
                o_phone = row.get('전화번호')
                latitude = row.get('위도')
                longitude = row.get('경도')

                if not o_name:  
                    continue
                
                if not latitude or not longitude:
                    continue

                sql = """
                    INSERT INTO oil (o_name, o_addr, o_phone, latitude, longitude)
                    VALUES (%s, %s, %s, %s, %s)
                """

                cursor.execute(sql, (o_name, o_addr, o_phone, latitude, longitude))
                insert_count += 1

            db.conn.commit()
            print(f'주유소 데이터 {insert_count}건 저장 완')

    except FileNotFoundError:
        print("CSV 파일을 찾을 수 없음")
    except Exception as e:
        print(f"오류 발생: {e}")
        db.conn.rollback()  # 에러 나면 되돌리기 

    finally:
        cursor.close()


# 착한 주유소 데이터 삽입
if db.conn:
    cursor = db.conn.cursor()

    try:
        with open("data/good_oil_info.csv", "r", encoding = 'utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)

            insert_count = 0
            for row in reader:
                g_name = row.get('o_name')
                g_addr = row.get('o_addr')
                g_phone = row.get('o_phone')
                gasoline_price = row.get('gasoline_price')
                diesel_price = row.get('diesel_price')

                if not g_name:  
                    continue
                
                if not gasoline_price or not diesel_price:
                    continue

                sql = """
                    INSERT INTO goodoil (g_name, g_addr, g_phone, gasoline_price, diesel_price)
                    VALUES (%s, %s, %s, %s, %s)
                """

                cursor.execute(sql, (g_name, g_addr, g_phone, gasoline_price, diesel_price))
                insert_count += 1

            db.conn.commit()
            print(f'착한 주유소 데이터 {insert_count}건 저장 완')

    except FileNotFoundError:
        print("CSV 파일을 찾을 수 없음")
    except Exception as e:
        print(f"오류 발생: {e}")
        db.conn.rollback()  # 에러 나면 되돌리기 

    finally:
        cursor.close()
        db.close()
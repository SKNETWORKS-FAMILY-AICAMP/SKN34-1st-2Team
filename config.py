import os
from dotenv import load_dotenv

load_dotenv()

# 왼쪽 os.getenv("DB_HOST")값은 .env파일 값 불러오기 
# 오른쪽 "localhost" 값은 기본값으로 .env파일 사용 안할 시 본인 환경에 또는 팀 공유사항 대로 수정
API_KEY = os.getenv("API_KEY") if os.getenv("API_KEY") else "d3c50f72560e702df41c006c8dbf049cf4e8fd3c415f0ed01fb3352ac010ddc8"
DB_HOST = os.getenv("DB_HOST") if os.getenv("DB_HOST") else "localhost"
DB_USER = os.getenv("DB_USER") if os.getenv("DB_USER") else "root"
DB_PASSWORD = os.getenv("DB_PASSWORD") if os.getenv("DB_PASSWORD") else "1234"
DB_NAME = os.getenv("DB_NAME") if os.getenv("DB_NAME") else "test"
KAKAO_MAP_KEY = os.getenv("KAKAO_MAP_KEY") if os.getenv("KAKAO_MAP_KEY") else "40cfabb95218e3ae03284f1df1282720"
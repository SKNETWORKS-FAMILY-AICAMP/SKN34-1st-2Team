import os
import math
import time
import pickle
import requests
import config as cf

class Api:
    #캐시파일 경로
    CACHE_DIR = "data/cache"
    #캐시파일 만료일 - 7일
    CACHE_EXPIRE = 60 * 60 * 24 * 7
    
    #api 불러오기 메서드
    def connect(self, kind):
        API_INFO = {
            "parking": {
                "url": "https://api.data.go.kr/openapi/tn_pubr_prkplce_info_api",
                "cache": "parking.pkl"
            },
            "gas": {
                "url": "https://api.data.go.kr/openapi/tn_pubr_public_conm_api",
                "cache": "gas.pkl"
            }
        }
        
        #캐시파일 생성
        info = API_INFO[kind]
        url = info["url"]
        cache_file = os.path.join(self.CACHE_DIR, info["cache"])
        
        os.makedirs(self.CACHE_DIR, exist_ok=True)
        
        #캐시파일이 존재여부 확인
        if os.path.exists(cache_file):
            file_time = os.path.getmtime(cache_file)
            now = time.time()
            
            #캐시파일 만료일 확인 
            if now - file_time < self.CACHE_EXPIRE:
                with open(cache_file, 'rb') as f:
                    return pickle.load(f)
                
        params = {
            "serviceKey": cf.API_KEY,
            "pageNo": 1,
            "numOfRows": 1,
            "type": "json"
        }

        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            raise Exception('API 호출 에러: ', response.status_code)
        
        data = response.json()
        
        #api 데이터의 총 개수를 구하고 1000개를 기준으로 페이지 구하기
        total_count = int(data["response"]["body"]["totalCount"])
        total_page = math.ceil(total_count / 1000)
        
        all_items = []

        #페이지 수 만큼 돌리고 모든 정보 저장
        for page in range(1, total_page + 1):
            params = {
                "serviceKey": cf.API_KEY,
                "pageNo": page,
                "numOfRows": 1000,
                "type": "json"
            }
            
            response = requests.get(url, params=params)
            data = response.json()

            items = data['response']['body']['items'] 
            
            all_items.extend(items)
        
        #캐시 파일 덮어쓰기
        with open(cache_file, 'wb') as f:
            pickle.dump(all_items, f)
            
        return all_items
    
    #주소 검색 메서드
    def search_address(self, kind, keyword):
        data = self.connect(kind)
        result = []

        #지번, 도로명 검색
        for item in data:
            if item.get('lnmadr', "").startswith(keyword) or item.get('rdnmadr', "").startswith(keyword):
                result.append(item)

        return result

api = Api()
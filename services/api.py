import requests
import config as cf

class Api:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        url = "https://api.data.go.kr/openapi/tn_pubr_prkplce_info_api"
        # url = "https://api.data.go.kr/openapi/tn_pubr_public_conm_api"

        params = {
            "serviceKey": cf.API_KEY,
            "pageNo": 1,
            "numOfRows": 18527,
            "type": "json"
        }

        response = requests.get(url, params=params)

        # st.write(response.status_code)

        if response.status_code == 200:
            data = response.json()
            result = data
        else:
            result = "실패"
            
        return result

api = Api()
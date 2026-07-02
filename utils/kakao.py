import config as cf
import requests

def address_to_latlng(address):
    url = "https://dapi.kakao.com/v2/local/search/address.json"

    headers = {
        "Authorization": f"KakaoAK {cf.KAKAO_REST_API_KEY}"
    }

    params = {
        "query": address
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None, None

    data = response.json()

    if len(data["documents"]) == 0:
        return None, None

    return (
        float(data["documents"][0]["y"]),
        float(data["documents"][0]["x"])
    )
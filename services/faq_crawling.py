import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. 크롬 드라이버 설정 및 오피넷 접속
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.opinet.co.kr/user/cufaq/cufaqSelect.do")
time.sleep(3) # 초기 페이지 로딩 대기

data_list = []

# 2. 1페이지부터 4페이지까지 반복 (페이지네이션)
for page_num in range(1, 5):
    print(f"--- {page_num}페이지 수집 시작 ---")
    
    # 자바스크립트로 페이지 이동 
    driver.execute_script(f"fn_egov_link_page({page_num})")
    time.sleep(2.5) # 페이지 이동 후 로딩 대기
    
    # 3. 현재 페이지의 모든 제목 요소 찾기
    # F12로 확인한 목록 제목의 CSS 선택자: td.t_left.input a
    try:
        title_elements = driver.find_elements(By.CSS_SELECTOR, "td.t_left.input a")
    except:
        print(f"{page_num}페이지 제목 로딩 실패.")
        continue

    # 4. 각 제목을 클릭하여 상세 내용 가져오기 (루프)
    for index in range(len(title_elements)):
        # 페이지가 바뀌면 요소가 초기화되므로 루프 안에서 다시 찾아야 함 (stale 에러 방지)
        current_titles = driver.find_elements(By.CSS_SELECTOR, "td.t_left.input a")
        
        try:
            target_title = current_titles[index]
            title_text = target_title.text
            print(f"  - '{title_text}' 클릭 중...")
            
            # 클릭하여 상세 페이지 이동
            target_title.click()
            time.sleep(1.5) # 상세 페이지 로딩 대기

            # 5. 상세 내용 추출 (F12로 확인한 본문 클래스: view_contents)
            content_element = driver.find_element(By.CLASS_NAME, "view_contents")
            content_text = content_element.text
            
            # 데이터 저장
            data_list.append({
                "페이지": page_num,
                "제목": title_text,
                "내용": content_text
            })
            print(f"    -> 내용 수집 완료 (글자수: {len(content_text)})")

            # 6. 목록 페이지로 복귀
            driver.back()
            time.sleep(1.5) # 목록으로 돌아온 후 로딩 대기

        except Exception as e:
            print(f"    [경고] 상세 수집 중 에러 발생: {e}")
            # 에러 발생 시 목록으로 돌아가도록 시도
            try:
                driver.back()
                time.sleep(1.5)
            except:
                pass

# 작업 완료 후 브라우저 종료
driver.quit()
print("==============================")
print(f"총 {len(data_list)}개의 FAQ 데이터를 수집했습니다.")

# 7. 엑셀 파일로 저장 
# Pandas DataFrame을 사용하여 깔끔하게 엑셀로 내보냅니다.
df = pd.DataFrame(data_list)
# 파일명
file_name = "../data/faq_data.xlsx"
df.to_excel(file_name, index=False)

print(f"데이터가 '{file_name}' 파일로 성공적으로 저장되었습니다.")

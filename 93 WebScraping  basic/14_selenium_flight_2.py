from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights"
# url = "https://flight.naver.com/"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 27일, 다음 달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번 달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음 달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 click
browser.find_element_by_link_text("항공권 검색").click()

# 기다림
try:
  elem = WebDriverWait(browser, 10).ultil(EC.presence_of_element_located(By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))
  # 성공했을 때 동작 수행
  print(elem.text)
finally:
  browser.quit()

# 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
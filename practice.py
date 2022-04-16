

from operator import truediv
from this import d
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.kdclub.com/kdabrd/main.php?board=jj004")
driver.implicitly_wait(10)
'''
#무한 스크롤
before_h = driver.execute_script("return document.body.scrollHeight")

while True:
    #맨아래로 스크롤을 내린다.ß
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    after_h = driver.execute_script("return document.body.scrollHeight")
    if after_h == before_h:
        break
    before_h = after_h
'''
'''
#프레임 이동
frame1 = driver.find_element(By.XPATH, "/html/frameset/frame[1]")
driver.switch_to.frame(frame1)
time.sleep(1)
'''
#로그인 창을 찾아 변수에 저장
login_id = driver.find_element(By.NAME, "input_id")
login_pw = driver.find_element(By.NAME, "password")

#search 변수에 저장된 곳에 값을 전송
login_id.send_keys("tjdgk3575")
login_pw.send_keys("clscjr20")
login_id.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

#식단페이지로 이동
driver.get("https://www.kdclub.com/kdabrd/main.php?board=data1")
driver.implicitly_wait(10)
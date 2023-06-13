import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 웹드라이버 설치 및 설정
chrome_options = webdriver.ChromeOptions()

# user 로 보이기위한 user_agent// 각자의 컴퓨터에 맞게 확인 필요
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
chrome_options.add_argument('user-agent=' + user_agent)

chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

url = 'https://autobell.co.kr/buycar/searchList?certi=N&filterKey=-1719297789&filterTab=0&homeSvc=N&listType=card&order=upd_dt&tab=0&viewType=0'

df_cars=[]

count = -1

# 크롬 열기 및 주소입력
driver.get(url)
driver.implicitly_wait(5)
time.sleep(1)

# 매물 선택
driver.find_element(By.XPATH, '//*[@id="thumbnail"]/yt-image/img').click()
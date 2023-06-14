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
driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div/div[2]/ul/li[1]/div/div[1]/div/span/div').click()

driver.implicitly_wait(5)
time.sleep(2)


info=["이름","차량번호","링크","연식","주행거리","연료","배기량","색상","보증정보","가격","신차대비가격"]

coloptions=["옵션_선루프","옵션_파노라마선루프","옵션_열선앞","옵션_열선뒤","옵션_전방센서"
     ,"옵션_후방센서","옵션_전방캠","옵션_후방캠","옵션_어라운드뷰","옵션_네비순정"]

findoptions=["선루프","선루프(파노라마)","열선시트(앞)","열선시트(뒤)","전방감지센서"
     ,"후방감지센서","전방카메라","후방카메라","어라운드뷰","네비게이션"]

colacci_info1=["보험이력등록","소유자변경횟수","사고상세_전손","사고상세_침수전손","사고상세_침수분손","사고상세_도난","보험_내차피해(횟수)","보험_내차피해(가격)","사고상세_타차가해(횟수)","보험_내차피해(가격)"]

cols=info+coloptions+colacci_info1
    #링크추가: 아웃라이어인지 확인하기 위해


#옵션이름 받아서 있는지 없는지 확인
def option_check(soupobject,option_name):
    check = soupobject.find("button", text=option_name).find_parent().find_previous_sibling().get_attribute_list('checked')

    if check[0]=='':
        return '유'
    else:
        return '무'
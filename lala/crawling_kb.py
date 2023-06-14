import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# kb 차차차 스크롤링
# kb차차는 인천, 수원 지역 매물이 주로 올라온다.
# 전체 매물은 약 15만 건이나 크롤링 테스트 용도로 kb차차차를 거치지 않는 직거래(약 1000개의 데이터)를 크롤링 하겠다.

# bs4 : 정적인 HTML을 파싱. JS같은 기능을 처리하는데는 한계
# selenium : 웹 driver를 활용한 웹 자동화 도구
# 차차차의 경우 목록을 클릭해야 상세 페이지로 넘어가기 때문에 셀레니움을 같이 사용해야할 것

# 크롬 웹드라이버 설치 및 설정
chrome_options = webdriver.ChromeOptions()


# user 로 보이기위한 user_agent// 각자의 컴퓨터에 맞게 확인 필요
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
chrome_options.add_argument('user-agent=' + user_agent)

chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

url = 'https://www.kbchachacha.com/public/search/main.kbc#!?page={}&sort=-orderDate&directYn=Y'

df_cars=[]

# page번호를 파라미터로 받은 url들을 모아두는 변수
urls=[]

# max페이지넘버를 담는 변수 | 23-06-13 기준 직거래 매물은 40페이지 까지 존재한다.
maxPage= 40

for page in range(maxPage):
    url= url.format(str(page))
    urls.append(url)

info=["이름","차량번호","링크","연식","주행거리","연료","배기량","색상","보증정보","가격","신차대비가격"]

coloptions=["옵션_선루프","옵션_파노라마선루프","옵션_열선앞","옵션_열선뒤","옵션_전방센서"
     ,"옵션_후방센서","옵션_전방캠","옵션_후방캠","옵션_어라운드뷰","옵션_네비순정"]

findoptions=["선루프","파노라마선루프","열선시트(앞좌석)","열선시트(뒷좌석)","전방센서"
     ,"후방센서","전방카메라","후방카메라","어라운드뷰","네비게이션(순정)"]

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
    
#모든 url마다 실행
for url in urls:
    res=requests.get(url)
    res.raise_for_status() # 응답 상태 코드를 확인하는 함수 | 오류 코드일 경우 예외를 발생시킨다. | 따로 예외처리를 하지 않았으므로 기본적인 예외 처리를 한다.
    requests.adapters.DEFAULT_RETRIES = 100000 # 요청 실패시 재시도 횟수를 설정한다. | 큰 값을 할당하여 실행 시간이 늘어날 수 있다.
    soup=BeautifulSoup(res.text,"lxml")

    cars=soup.find_all("li",attrs={"class":"product-item"})
    links=[]
    #한 url마다 들어있는 모든 차들에 대해 실행
    for car in cars:
        link = "https://www.bobaedream.co.kr" + car.a["href"]
        links.append(link)
    for link in links:
        print(link)

        res2=requests.get(link,timeout=5)
        res2.raise_for_status()
        soup2 = BeautifulSoup(res2.text, "lxml")
        infobox = soup2.find("div", attrs={"class": "info-util box"})
        try:
            ratiopr = infobox.find("b")
        except:
            continue

        name=soup2.find("h3",attrs={"class":"tit"})
        state=soup2.find("div",attrs={"class":"tbl-01 st-low"})
        galdata=soup2.find("div",attrs={"class":"gallery-data"})
        carnumber=galdata.find("b")

        year=state.find("th",text='연식').find_next_sibling("td")
        km=state.find("th",text='주행거리').find_next_sibling("td")
        fuel=state.find("th",text='연료').find_next_sibling("td")
        amount=state.find("th",text='배기량').find_next_sibling("td")
        color=state.find("th",text='색상').find_next_sibling("td")
        guarn=state.find("b",text='보증정보').find_next("td")
        price=soup2.find("span",attrs={"class":"price"})

        option_table=soup2.find("div",attrs={"class":"tbl-option"})
        checkoptions=[]
        if option_table.find("th",text='외관')!=None:
            for option in findoptions:
                checkoptions.append(option_check(option_table,option))
        else:
            checkoptions=['']*len(coloptions)

        if infobox.find("span",attrs={"class":"round-ln insurance"}).find_next("i").find_next("em")==None:
            acc1 = '미등록'
        else:
            acc1 = '등록'


        findacci_info1=[]
        try:
            if acc1=='등록':
                acc1table=soup2.find("div",attrs={"class":"info-insurance"})
                insurdt1=acc1table.find("th",text="차량번호/소유자변경").find_next_sibling("td").get_text()[-2]
                insuraccis1 = acc1table.find("th", text="자동차보험 특수사고").find_next_sibling("td").get_text().split('/')
                insurdt2=insuraccis1[0][-2]
                insurdt3 = insuraccis1[1][-2]
                insurdt4 = insuraccis1[2][-2]
                insurdt5 = insuraccis1[3][-1]
                insuraccis2=acc1table.find("th", text="보험사고(내차피해)").find_next_sibling("td").get_text().split('회')
                insurdt6=insuraccis2[0]
                insurdt7=insuraccis2[1][2:-2]
                insuraccis3=acc1table.find("th", text="보험사고(타차가해)").find_next_sibling("td").get_text().split('회')
                insurdt8=insuraccis3[0]
                insurdt9=insuraccis3[1][2:-2]
                findacci_info1=[insurdt1,insurdt2,insurdt3,insurdt4,insurdt5,insurdt6,insurdt7,insurdt8,insurdt9]
            else:
                findacci_info1=['']*(len(colacci_info1)-1)
        except:
            findacci_info1 = [''] * (len(colacci_info1)-1)
        temp=[name.get_text(),carnumber.get_text(),link,year.get_text(),km.get_text(),fuel.get_text(),amount.get_text(),
          color.get_text(),guarn.get_text(),price.get_text(),ratiopr.get_text()]+checkoptions+[acc1]+findacci_info1
        df_cars.append(temp)
df_cars=pd.DataFrame(data=df_cars,columns=cols)
df_cars.to_csv('cars.csv')
print(df_cars.head())
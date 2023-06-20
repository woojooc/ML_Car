# 📖 프로젝트명

### ✔️ 수입 중고차 가격 예측 프로젝트 (메티버스 아카데미 2기 AI반 ML 프로젝트)

# 📃 프로젝트 소개 

### ✔️ 머신러닝(XGBoost/LightGBM, RandomFroest, LinearRegression, Lasso/Lidge)을 활용한 수입 (외제) 중고차 가격 예측 프로젝트입니다.  

국내 자동차 시장에서 중고차 시장은 신차 시장에 비해 2배 이상의 규모를 차지하고 있습니다. 또한 수입차(외제차)의 보편화로 인한 수입차 점유율 증가 추세로 중고 수입차 가격에 대해 신뢰할 수 있는 지표가 필요한 시점입니다.
이번 프로젝트를 통해 중고 수입차 시장의 구매자, 판매자 모두에게 합리적인 가격 선정의 근거를 제공하여 수입차 중고 거래 활성화를 도모할 수 있을 것입니다. 

# 👩‍🔧 팀원 소개 및 역할

### ✔️ 팀원
메타버스 아카데미 2기 AI반 라경훈, 김우정, 임정민, 서주완 등 총 4명

### ✔️ 역할 분담
모든 팀원들의 전반적인 머신러닝 프로젝트 프로세스 경험을 위해 데이터 수집/전처리, EDA , 모델링, 파라미터 튜닝, 인사이트 도출 등을 각각 수행하였습니다. 각 팀원별 이름 (lala,wj,jm,jw)으로 branch를 나누어 기록하였습니다. 단, 주요 머신러닝 모델들(XGBoost/LightGBM, RandomFroest, LinearRegression, Lasso)을 전담하여 학습하고 비교하였습니다.

LinearRegression : 라경훈

Lasso : 김우정

RandomForest : 임정민

XGBoost/LightGBM : 서주완


# 📅프로젝트 진행 기록

### ✔️ 수행 기간
2023.06.13 ~ 2023.06.21

### ✔️ 세부 진행 기록
- 23-06-12 : 회의 및 주제 정하기, 보배드림 데이터 크롤링
- 23-06-13 : Dacon 데이터 수집, EDA
- 23-06-14 : PPT 초안 작성, EDA, 워드클라우드
- 23-06-15 : 머신 러닝 회귀 모델링 (XGBoost/LightGBM, RandomForest, LinearRegression, Lasso)
- 23-06-16 : K-Fold 학습, GridSearchcv 하이퍼파라미터 튜닝 학습 후 비교
- 23-06-19 : GridSearchcv 하이퍼파라미터 튜닝, AutoML (Pycaret) 학습, PPT 수정
- 23-06-20 : AutoML(Optuna, Autogluon)학습, 각 모델별 MAE 비교, 인사이트 도출 , PPT 수정, 발표 대본 작성 
- 23-06-21 : PT 발표 및 질의응답


# 📊 데이터 소개
### ✔️ Dacon '데이콘 Basic 자동차 가격 예측 AI 경진대회' 데이터셋을 활용하였습니다.
[데이콘 Basic 자동차 가격 예측 AI 경진대회](https://dacon.io/competitions/official/236114/overview/description) <br><br>

![image](https://github.com/woojooc/ML_Car/assets/115389344/66e2a813-ab89-4802-92a7-8d49f6fe1173)


### ✔️ 데이터 세부 사항
데이터 갯수 : 57920개<br>
ID : 샘플 별 고유 id<br>
생산년도 : 차량이 생산된 연도<br>
모델출시년도 : 차량의 모델이 처음으로 출시된 연도<br>
브랜드<br>
차량모델명<br>
판매도시 : 3글자로 인코딩된 도시 이름<br>
판매구역 : 3글자로 인코딩된 구역 이름<br>
주행거리 : 총 주행 거리(km)<br>
배기량 : 내연기관에서 피스톤이 최대로 밀어내거나 빨아들이는 부피 (cc)<br>
압축천연가스(CNG) : 압축천연가스(CNG) 자동차 여부<br>
경유 : 경유 자동차 여부<br>
가솔린 : 가솔린 자동차 여부<br>
하이브리드 : 하이브리드 자동차 여부<br>
액화석유가스(LPG) : 액화석유가스(LPG) 자동차 여부<br>
가격 : 자동차 가격(백만원)<br>

# 💡 주요 내용


# 🛠 기술 스택

### ▪ 언어
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

### ▪ 주요 라이브러리
<img src="https://img.shields.io/badge/scikit learn-F7931E?style=for-the-badge&logo=scikit learn&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/seaborn-99CC00?style=for-the-badge&logo=seaborn&logoColor=white"> <img src="https://img.shields.io/badge/matplotlib-0058CC?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/wordcloud-FF4F8B?style=for-the-badge&logo=wordcloud&logoColor=white">
<img src="https://img.shields.io/badge/konlpy-FF0000?style=for-the-badge&logo=konlpy&logoColor=white"> <img src="https://img.shields.io/badge/collections-7FADF2?style=for-the-badge&logo=collections&logoColor=white">

### ▪ 개발 툴
<img src="https://img.shields.io/badge/VS code-2F80ED?style=for-the-badge&logo=VS code&logoColor=white"> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white">

### ▪ 협업 툴
<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"> <img src="https://img.shields.io/badge/Google Slides-FFBB00?style=for-the-badge&logo=Google Slides&logoColor=white">

# 🔍 참고 자료
### ✔️ 데이터
  
[데이콘 Basic 자동차 가격 예측 AI 경진대회](https://dacon.io/competitions/official/236114/overview/description)

### ✔️ 논문
1) 고찬영, 2021, 다중선형회귀분석을 이용한 중고차 가격 예측 연구 : A사의 사례를 중심으로』, 인하대학교 물류전문대학원 석사학위 논문
2) Sümeyra MUTİ1, Kazım YILDIZ2, 2023, Using Linear Regression For Used Car Price Prediction
,International Journal of Computational and
Experimental Science and ENgineering
,Vol. 9-No.1 (2023) pp. 11-16





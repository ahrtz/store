# SSAFY Bigdata project

## 01. 파이썬 가상환경 구성 (2020.09.07.월)
```sh
python -m venv testing
cd testing
Scripts\activate.bat
cd ..
```

## 02. pdfminer 설정 (2020.09.07.월 -> pdf 파일을 html로 만들어주는 모듈)
```sh
가상환경이 실행된 후 실행한다.
pip install tika
python mode_pdfconvert.py

요약하는 방법 중 하나를 사용한다.
python mode_summarize.py
```

## 09/08

##### Vuetify 활용
제공되는 layout 이용하면 간단하게 화면 구성 가능할 듯

##### Excel -> 하나로 이어붙이기
하나의 Excel파일로 하기로 했지만, for문으로 file들 읽어서 DB에 저장하면 어떨까 테스트

## 09/09

##### Vuetify 활용
Vuetify에서 제공하는 file input, tab 기능 활용

##### Wordcloud 적용
vue-worldcloud 이용하여 간단하게 만들 수 있음

##### SSAFY-SR 프로젝트 발대식
이제 더 바빠질 듯

## 09/10 ~ 09/11

##### 텍스트 유사도 계산 알고리즘
TF-IDF와 코사인 유사도 이용하여 Abstract의 유사도 검사
대부분 10% 미만의 유사도지만 데이터가 300개뿐이라 아직 제대로 되는 건지 확인 못함

##### 팀 미팅
PDF 변환(텍스트, 이미지, 표 에서 중요도 순으로 먼저 하는 게 좋을 듯)
요약 알고리즘
추천 알고리즘 (텍스트 유사도가 어렵다면, like로 유사 논문 검색 + 협업 필터링)

요약, 추천 중에서 현실적인 시간 따져서 중요도 생각해볼 것

협업 필터링 - 스크랩 횟수, 접속 로그 + 접속 시간, 원문 보기

이게 다 될까...?

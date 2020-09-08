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

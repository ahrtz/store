# SSAFY Bigdata project

## 01. 파이썬 가상환경 구성 (2020.09.07.월)
```sh
python -m venv testing
cd testing
Scripts\activate.bat
cd ..
```

```python

#윈도우일때
python -m venv venv
source venv/Scripts/activate.bat
# 가상환경에 패키지 설치 
pip install -r requirements.txt

```

## 02. pdfminer 설정 (2020.09.07.월 -> pdf 파일을 html로 만들어주는 모듈)
```sh
가상환경이 실행된 후 실행한다.
pip install tika
python mode_pdfconvert.py

요약하는 방법 중 하나를 사용한다.
python mode_summarize.py
```
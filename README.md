# SSAFY Bigdata project

## Commit Rule
1. __branch 종류__
  - __develop-_[이니셜]___ : 각 개발자들이 작업하는 개인 공간.
2. __Commit 메세지 Format__  
  ___"[type]commit message, [issue Key] "___  
  _ex) git commit -m "[Add] <기능설명>, [jira Key]"_
  - __Add :__ 새로운 기능 추가.
  - __Fix :__ 버그 수정.
  - __Modify :__ 기능에 버그는 없지만, 코드 수정.
  - __Test :__ 테스트용 코드.
  - __Style :__ 단순 코드 포멧팅.(세미콜론 누락, 들여쓰기 등).
  - __Doc :__ 문서(.md 등) 수정.

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
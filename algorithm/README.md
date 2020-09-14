# SSAFY Bigdata project

## 01. 파이썬 가상환경 구성 (2020.09.07.월)
```sh
python -m venv testing
cd testing
Scripts\activate.bat
cd ..
```

## 02. pdfminer 설정 (2020.09.07.월 ~ 09.11.금 -> pdf 파일을 html로 만들어주는 모듈)
```sh
가상환경이 실행된 후 실행한다.
pip install pdfminer.six
python mode_pdfconvert.py

요약하는 방법 중 하나를 사용한다.
python mode_summarize.py


관련 문제 : tika Application은 시간이 너무 많이 걸리며,
GNU 프로젝트로 논문 요약 버전을 가져오는 것은 제대로 동작하지 않는다.
```
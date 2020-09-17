# SSAFY 특화 프로젝트 (논문 추출 프로젝트)

## 01. 파이썬 가상환경 구성 (2020.09.07.월)
```sh
python -m venv testing
cd testing
Scripts\activate.bat
cd ..
```

## 02. PDFFile Parsing 하는 방법 -> 시도 한 방법 전부 소개 (2020.09.07.월 ~ 09.16.수 -> pdf 파일을 Parsing)
```sh
* CERMINE을 이용 PDF논문 추출 테스트 방법
참조 사이트 : https://zelkun.tistory.com/entry/CERMINE-114snapshot%EC%9D%B4%EC%9A%A9-PDF%EB%85%BC%EB%AC%B8-%EC%B6%94%EC%B6%9C-%ED%85%8C%EC%8A%A4%ED%8A%B8

공식 사이트 : http://cermine.ceon.pl

- GNU라이센스라서 이 프로그램은 사용 불가 한 줄 알았으나, SSAFY 내에 물어본 결과 사용 가능한 걸로 확인되었습니다.
- 그러나 논문 메타 추출 프로그램에서 KCI 논문을 추출해보니 시간이 지나치게 많이 드는 문제가 일어났습니다.
- 또한 한글 논문이라서 정확히 다 추출이 되지 않아서 다른 방법을 찾아보기로 했습니다.

* GROBID를 이용 PDF논문 추출 테스트 방법
- 위 방법도 마찬가지로 한글 논문이라서 정확히 다 추출이 되지 않았습니다.


-> 결론 : PDF에서 기존 논문 내용을 구분하는 방법은 한글 논문에는 다른 방법이 없어서, 직접 추출해야 하는걸로 결론 지었습니다.
```

```sh
* PDF -> Text 변환 추출 테스트 방법

- PyPDF2
- 바이트 스트림으로 파일을 열어서, PDF의 파일 정보와 텍스트를 가져올 수 있는 모듈
- 사용하기 어렵지 않았으나, PDF 논문 파일에는 이게 제대로 적용이 되지 않았습니다.
- 띄어쓰기가 날라가고, 정확성이 떨어지며, 일부 논문에서 한글 깨짐 현상이 일어났습니다.

- pdftotext
- PDF문서의 텍스트만 필요하다고 하면 이 패키지를 사용
- 간단한 패키지이며, 따로 설치가 많이 필요하지 않았지만, 정확성이 떨어지는 문제가 일어났습니다.
- 위 문제는 머신러닝 기법이 들어간 pdf -> text 기법을 사용하기로 했습니다.

- pdftotree
- pdftotree는 pdf문서에 텍스트, 그림, 표를 추출해서 문서의 구조를 유지하여 html로 만들어주는 모듈
- 현재 논문에서 있는 table 전부 구분 가능
- 하지만 코덱 문제 때문에 일부 논문을 읽지 못하는 문제 발생 (테스트 파일의 약 10%)
- 또한 시간이 많이 걸리기 때문에, 대안 패키지를 사용하기로 했습니다.

- pdfminer
- 설치 방법 : pip install pdfminer.six (머신러닝 모듈이 들어가, 시간이 매우 많이 걸립니다.)
- pdf문서를 text나 html로 변경해주는 모듈
- table 구분 X, 그림 추출 X, 텍스트 정확도는 높고, 시간이 빠릅니다.
- 그래서 여러 문제점이 높지만, pdfminer를 사용하고, 따로 table 추출 모듈을 통해서 구분하기로 했습니다.

- hanspell
- 설치 방법 : pip install py-hanspell / git clone 이후 python setup.py install
- 사이트 : https://github.com/ssut/py-hanspell
- py-hanspell은 네이버 맞춤법 검사기를 이용한 파이썬용 한글 맞춤법 검사 라이브러리입니다.
- pdfminer + hanspell을 통한 맞춤법 검사를 하기로 했습니다
```

```sh
- tabula
- tabula-java가 원형이며, 입출력 파일을 가공 가능
- 현재 논문 PDF에서 table 인식이 불가능 합니다.

- camelot
- 가장 많이 사용하는 라이브러리
- 현재 논문 PDF에서 table 인식이 불가능 합니다.

- PDFPlumber
- 옵션도 많고, 지원하는 기능도 많습니다.
- 현재 논문 PDF에서 table 인식이 불가능 합니다.

- OCR_SPACE
- OCR 기반의 table 추출 API
- 25,000회 제한, API 표 인식 불가

- PDF_Tables
- 25회 제한, API
- 기존 텍스트까지 표로 인식하는 문제 발생
```

## 03. PDF Install
```sh
pip install pdfminer.six

git clone https://github.com/ssut/py-hanspell
cd hanspell
python setup.py install
cd ..

pip install re
pip install itertools
pip install collections
pip install fitz
pip install gensim newspaper3k

pip install wordcloud
pip install matplotlib
pip install konlpy

https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
사이트에서 자신에 맞는 wordcloud 파일 다운로드
pip install wordcloud-1.8.0-cp36-cp36m-win_amd64.whl
```
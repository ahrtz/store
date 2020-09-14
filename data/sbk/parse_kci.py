import os

import pandas as pd
import xlrd
import requests
import json
from googletrans import Translator

DATA_DIR = "."
DATA_FILE = os.path.join(DATA_DIR, "논문검색리스트 정제 (1).xls")
DUMP_FILE = os.path.join(DATA_DIR, "dump.pkl")

paper_columns = (
    "id",    # pk
    "title_ko",   # 논문명
    "title_en",
    "author",  # 저자
    "coauthor",    # 공동저자
    "journal_name_ko",  # 학술지 명
    "journal_name_en",
    "issuer_ko",   # 발행기관 명
    "issuer_en",
    "year",    # 발행년
    "volume",    # 권
    "page",    # 페이지
    "keyword",  # 키워드
    "subject",    # 주제 분야
    "quotation",   # 피인용횟수
    "url",  # url
    "doi",  # doi
    "abstract",    # 요약
)

keyword_columns = (
    #"id",   # pk
    "content",  # 키워드 내용
)


def import_data():
    """
    논문 데이터 파일을 읽어서 Pandas DataFrame 형태로 저장합니다
    """
    try:
        cnt = 0
        papers = []
        for i in range(1, 4):
            rb = xlrd.open_workbook("논문검색리스트 정제 ("+str(i)+").xls")
            rb_sheet = rb.sheet_by_index(0)

            nrows = rb_sheet.nrows
            ncols = rb_sheet.ncols

            for row in range(1, nrows):
                columns = []
                for col in range(0, ncols):
                    if col == 1 or col == 10 or col == 15 or col == 21:
                        continue
                    if col == 0:
                        columns.append(cnt)
                        cnt += 1
                        continue
                    columns.append(rb_sheet.cell_value(row, col))

                papers.append(columns)

    except FileNotFoundError as e:
        print(f"`{data_path}` 가 존재하지 않습니다.")
        exit(1)

    # print(papers)
    paper_frame = pd.DataFrame(data=papers, columns=paper_columns)

    # ·을 ,로 변경
    paper_frame["keyword"] = paper_frame.keyword.apply(lambda c: c.replace("·", ","))
    # print(paper_frame)
    return {"papers": paper_frame}


def parse_keyword(dataframes):
    """
    논문 데이터파일을 읽어서 keyword 파일로 저장합니다
    :param dataframe: 
    :return: 
    """
    papers = dataframes["papers"]

    keywords = papers.keyword.apply(lambda c: c.split(","))

    keywords_list = []
    for keyword in keywords:
        for word in keyword:
            keywords_list.append(word.strip())

    print(len(keywords_list))
    # print(keywords_list)
    keywords_set = set(keywords_list)
    # print(keywords_set)
    print(len(keywords_set))

    keyword_frame = pd.DataFrame(data=keywords_set, columns=keyword_columns)

    return {"papers": dataframes["papers"], "keywords": keyword_frame}


def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)


def translation_data(dataframes):
    """
    영문을 Google Translation API 를 이용해 한글로 번역
    :param dataframes: 
    :return: 
    """
    papers = dataframes["papers"]
    keywords = dataframes["keywords"]

    title_ko = papers["title_ko"]
    title_en = papers["title_en"]
    translator = Translator()

    for i in range(0, 900):   # len(title_ko)
        # 어떤 언어인지 확인
        str_title_ko = title_ko[i]
        str_title_en = title_en[i]
        title_ko_lang = ""
        title_en_lang = ""
        if str_title_ko != "":  title_ko_lang = translator.detect(str_title_ko).lang
        if str_title_en != "":  title_en_lang = translator.detect(str_title_en).lang

        if title_ko_lang == 'ko' and title_en_lang == 'en':     # 두개 다 있는 경우
            continue
        elif title_ko_lang == 'en' and title_en_lang == 'ko':   # 두개 위치가 바뀐 경우
            papers.loc[i, 'title_ko'] = str_title_en
            papers.loc[i, 'title_en'] = str_title_ko
        elif title_ko_lang == 'en':                             # 영어인 경우
            title_trans = translator.translate(str_title_ko, dest="ko")
            papers.loc[i, 'title_ko'] = title_trans.text
            papers.loc[i, 'title_en'] = str_title_ko
        else:                                                   # 한글인 경우
            title_trans = translator.translate(str_title_ko, dest="en")
            papers.loc[i, 'title_en'] = title_trans.text

    # print(papers["title_ko"])
    # print(papers["title_en"])

    return {"papers": dataframes["papers"], "keywords": keywords}


if __name__ == '__main__':
    # data = xls_to_json()

    print("[*] Parsing data...")
    # data = import_data()
    print("[+] Done")

    print("[*] Parsing keyword...")
    # data = parse_keyword(data)
    print("[+] Done")

    data = load_dataframes()
    # data_trans = translation_data(data)

    print("[*] Dumping data...")
    # dump_dataframes(data_trans)
    print("[+] Done\n")

    print("[논문]")
    print(data["papers"].loc[:, ("title_ko", "title_en")])
    print("\n")

    print("[키워드]")
    # print(data["keywords"])
    print("\n")

    # # 파파고 번역
    # request_url = "https://openapi.naver.com/v1/papago/n2mt"
    # text = "Python is an easy to learn, powerful programming language. "
    #
    # # !! warning !! 꼭 지우기 !!
    # headers = {"X-Naver-Client-Id": "", "X-Naver-Client-Secret": ""}
    # params = {"source": "en", "target": "ko", "text": text}
    # response = requests.post(request_url, headers=headers, data=params)
    #
    # result_json = response.json()
    # print(result_json)
    # result = json.loads(result_json)
    #
    # print(result["translatedText"])

import os

import pandas as pd
import xlrd

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
        for i in range(1, 2):
            rb = xlrd.open_workbook(DATA_FILE)
            rb_sheet = rb.sheet_by_index(0)
    except FileNotFoundError as e:
        print(f"`{data_path}` 가 존재하지 않습니다.")
        exit(1)

    nrows = rb_sheet.nrows
    ncols = rb_sheet.ncols

    papers = []
    for row in range(1, nrows):
        columns = []
        for col in range(0, ncols):
            if col == 1 or col == 10 or col == 15 or col == 21:
                continue
            columns.append(rb_sheet.cell_value(row, col))

        papers.append(columns)

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

    print(keywords_list)
    keywords_set = set(keywords_list)
    print(keywords_set)

    keyword_frame = pd.DataFrame(data=keywords_set, columns=keyword_columns)
    
    return {"papers": dataframes["papers"], "keywords": keyword_frame}


def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)


if __name__ == '__main__':
    # data = xls_to_json()

    print("[*] Parsing data...")
    data = import_data()
    print("[+] Done")

    print("[*] Parsing keyword...")
    data = parse_keyword(data)
    print("[+] Done")

    print("[*] Dumping data...")
    dump_dataframes(data)
    print("[+] Done\n")

    data = load_dataframes()

    print("[논문]")
    print(data["papers"])
    print("\n")

    print("[키워드]")
    print(data["keywords"])
    print("\n")

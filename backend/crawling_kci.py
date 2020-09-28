import xlrd
import xlwt
from selenium import webdriver
import time
import requests
# from urllib.request import urlopen
import xml.etree.ElementTree as ET

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()
from reports.models import Summary_report


DOWNLAD_PATH = "C:/Users/multicampus/Downloads/"

def crawler_thesis_chk_setting(start, end):
    """
    kci checkbox setting
    :return:
    """
    path = "F://Install/chromedriver_win32/chromedriver"
    driver = webdriver.Chrome(path)

    url = "https://www.kci.go.kr/kciportal/po/member/popup/loginForm.kci"
    driver.get(url)
    driver.implicitly_wait(10)

    # 로그인 => 추후에 id, pw 지우기
    login = driver.find_element_by_name("uid")
    login.send_keys("ksb0925")
    login = driver.find_element_by_name("upw")
    login.send_keys("30286450")
    login.send_keys('\n')

    #
    search_link = driver.find_element_by_link_text("논문검색")
    search_link.send_keys('\n')

    search = driver.find_element_by_xpath("//*[@id='AKCFrm']/div/div[3]/div/input")
    search.send_keys('\n')

    # 더보기 누른 후 2010~2020년도 체크박스 누르기
    links = driver.find_elements_by_link_text('더보기')
    for link in links:
        link.click()

    # 분야 선택
    chk_major = driver.find_element_by_id("majorD")
    chk_major.click()
    chk_major = driver.find_element_by_id("majorC")
    chk_major.click()

    for i in range(0, 3):
        chk_year = driver.find_element_by_id("pubdt" + str(i))
        chk_year.click()
        # print(chk_year.is_selected())

    # 정규 논문 체크
    chk_regular = driver.find_element_by_id("artiY")
    chk_regular.click()

    # 체크항목 내에서 재검색 클릭
    driver.execute_script("facetedSearch()")

    # 300개 선택
    count = driver.find_element_by_xpath("//*[@id='sBody']/div[2]/div/div[2]/div/div[3]/ul/li[1]/a")
    count.send_keys('\n')
    driver.execute_script("reSearch()")

    # 페이지 마지막 번호 가져오기
    last_page = driver.find_element_by_xpath("//*[@id='sBody']/div[3]/div/div/div/a[6]")
    str_last_page = last_page.get_attribute('href')
    int_last_page = str_last_page.split('(')[1].split(')')[0]
    # print(int_last_page)

    # 다운로드할 페이지 설정해서 excel 다운 클릭
    for i in range(start, end):   # range(1, int_last_page) 추후에 모든 페이지 excel로 출력
        driver.execute_script("javascript:goPage("+str(i)+")")
        driver.find_element_by_id("checkAll").click()
        driver.execute_script("lf_exceldown()")
        time.sleep(10)
        print(i)


def extract_abstract_using_selenium():
    path = "F://Install/chromedriver_win32/chromedriver"
    driver = webdriver.Chrome(path)

    url = "https://www.kci.go.kr/kciportal/po/member/popup/loginForm.kci"
    driver.get(url)
    driver.implicitly_wait(10)

    # i: excel 번호
    for i in range(6, 7):
        rb = xlrd.open_workbook(DOWNLAD_PATH + "논문검색리스트Excel (" + str(i) + ").xls")
        rb_sheet = rb.sheet_by_index(0)
        nrows = rb_sheet.nrows
        ncols = rb_sheet.ncols

        result = []
        words = ["title_kor", "title_eng", "main_author", "sub_author", "journal_kor", "journal_eng",
                 "issuer_kor", "issuer_eng", "issue_year", "book_num", "page_num", "keyword_kor", "keyword_eng", "subject",
                 "quote", "direct_urls", "doi", "abstract"]
        for j in range(1, 301):  # range(1, 301) 추후에 모든 논문 상세페이지에서 abstract 추출
            papers = {}
            idx = 0
            for col in range(ncols):
                if col == 0 or col == 1 or col == 10:
                    continue
                papers[words[idx]] = rb_sheet.cell_value(j, col)
                idx += 1

            detail = driver.find_element_by_xpath(
                "//*[@id='poArtiSearList']/table/tbody/tr[" + str(j) + "]/td[2]/p/label/a")
            detail.send_keys('\n')
            try:
                abstract = driver.find_element_by_xpath("//*[@id='printArea']/div[2]/div[1]/div/p")
                papers["abstract"] = abstract.text
                # wb_sheet.write(j, ncols, abstract.text)
            except Exception as e:
                papers["abstract"] = ""
                print(e)
            driver.back()

            result.append(papers)

        # print(result)
        for item in result:
            Summary_report(
                title_kor=item['title_kor'],
                title_eng=item['title_eng'],
                main_author=item['main_author'],
                sub_author=item['sub_author'],
                # 저널 이름
                journal_kor=item['journal_kor'],
                journal_eng=item['journal_eng'],
                # 발행기관
                issuer_kor=item['issuer_kor'],
                issuer_eng=item['issuer_eng'],
                issue_year=item['issue_year'],
                book_num=item['book_num'],
                keyword_kor=item['keyword_kor'],
                keyword_eng=item['keyword_eng'],
                subject=item['subject'],
                quote=item['quote'],
                direct_urls=item['direct_urls'],
                doi=item['doi'],
                abstract=item['abstract'],
                page_num=item['page_num']
            ).save()


def extract_abstract_using_openAPI(start, end):
    # i: excel 번호
    for i in range(start, end):
        rb = xlrd.open_workbook(DOWNLAD_PATH + "논문검색리스트Excel (" + str(i) + ").xls")
        rb_sheet = rb.sheet_by_index(0)
        nrows = rb_sheet.nrows
        ncols = rb_sheet.ncols

        result = []
        words = ["title_kor", "title_eng", "main_author", "sub_author", "journal_kor", "journal_eng",
                 "issuer_kor", "issuer_eng", "issue_year", "book_num", "page_num", "keyword_kor", "keyword_eng",
                 "subject", "quote", "direct_urls", "doi", "abstract"]

        # 엑셀에 있는 모든 row
        for j in range(1, nrows):
            papers = {}
            idx = 0
            papers_kci_id = ""

            for col in range(ncols):
                # 논문 ID
                if col == 1:
                    papers_kci_id = rb_sheet.cell_value(j, col)
                    continue
                if col == 0 or col == 10:
                    continue
                
                papers[words[idx]] = "NaN"
                papers[words[idx]] = rb_sheet.cell_value(j, col)
                idx += 1

            # print(papers_kci_id)
            url = "https://open.kci.go.kr/po/openapi/openApiSearch.kci?key=19192000&apiCode=articleDetail&id=" + papers_kci_id
            response = requests.get(url=url)
            if(response.status_code == 200):
                xml = response.text
            else:
                continue

            # xml parsing
            tree = ET.ElementTree(ET.fromstring(xml))
            root = tree.getroot()
            
            # subject 중분류까지만 바꾸기
            categories = root.find('outputData').find('record').find('articleInfo').find('article-categories').text
            if categories is None:
                papers["subject"] = "NaN"
            else:
                categories_list = categories.split('>')
                if len(categories_list) > 1:
                    papers["subject"] = categories_list[1].strip()

            abstract = root.find('outputData').find('record').find('articleInfo').find('abstract')
            if abstract is None:
                papers["abstract"] = "NaN"
            else:
                papers["abstract"] = abstract.text
            # print(abstract.text)

            result.append(papers)

        print(str(i)+"번 엑셀까지 완료")
        # print(result)
        for item in result:
            Summary_report(
                title_kor=item['title_kor'],
                title_eng=item['title_eng'],
                main_author=item['main_author'],
                sub_author=item['sub_author'],
                # 저널 이름
                journal_kor=item['journal_kor'],
                journal_eng=item['journal_eng'],
                # 발행기관
                issuer_kor=item['issuer_kor'],
                issuer_eng=item['issuer_eng'],
                issue_year=item['issue_year'],
                book_num=item['book_num'],
                keyword_kor=item['keyword_kor'],
                keyword_eng=item['keyword_eng'],
                subject=item['subject'],
                quote=item['quote'],
                direct_urls=item['direct_urls'],
                doi=item['doi'],
                abstract=item['abstract'],
                page_num=item['page_num']
            ).save()

import sqlite3
import pandas as pd
DATA_DIR = 'F:/SSAFY/BigDataPJT/LAST/s03p23a406/data/sbk'
DUMP_FILE_ALL = os.path.join(DATA_DIR, "all_data.pkl")
DUMP_FILE_EN = os.path.join(DATA_DIR, "abstract_en.pkl")
DUMP_FILE_KO = os.path.join(DATA_DIR, "abstract_ko.pkl")
def sqlite_to_pandas():
    con = sqlite3.connect("./db.sqlite3")
    cur = con.cursor()
    query = cur.execute("SELECT * FROM reports_summary_report")
    cols = [column[0] for column in query.description]
    result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    result_ko = []
    result_en = []
    result_all = []

    for index, row in result.iterrows():
        if row.abstract is None:
            continue
        result_all.append(row)
        if isEnglishOrKorean(row.abstract):
            result_en.append(row)
        else:
            result_ko.append(row)
    
    endf = pd.DataFrame.from_records(data=result_en, columns=cols)
    kodf = pd.DataFrame.from_records(data=result_ko, columns=cols)
    alldf = pd.DataFrame.from_records(data=result_all, columns=cols)
    pd.to_pickle(endf, DUMP_FILE_EN)
    pd.to_pickle(kodf, DUMP_FILE_KO)
    pd.to_pickle(alldf, DUMP_FILE_ALL)
    print(len(result_en))
    print(len(result_ko))
    print(len(result_all))


def isEnglishOrKorean(input):
    for c in input:
        if ord('가') <= ord(c) <= ord('힣'):
            return False

    return True

if __name__ == '__main__':
    # crawler_thesis_chk_setting(26, 27)    # 시작 페이지, 끝페이지
    # extract_abstract_using_openAPI(26, 31)    # 시작 엑셀번호, 끝 엑셀번호
    sqlite_to_pandas()

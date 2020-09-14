import urllib.request
import urllib.parse
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# 됐다 안됐다 하는 불안정함있음. 디비에 구축하는 일회용으로 사용하는 게 좋아 보임...
# 그리고 각각의 논문 디테일 페이지 칼럼이 다 다릅니다. 어디엔 있는 것이 어디엔 없고 이런 식이기에 크롤링 불안정. 방법 있을지..

# 드라이버
# Optional argument, if not specified will search path.
path = 'C:/Users/multicampus/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)


# 일단 학위 논문만 크롤링. 학술, 해외, 국내 더 있습니다.

# 전체 페이지 수 찾기
baseUrl = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=computer&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount={}&orderBy=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&query='
plusUrl = urllib.parse.quote_plus(input('검색어 입력 : '))  # 한글 입력 가능
url = baseUrl.format(0) + plusUrl

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# 전체 논문 수 string형
count_temp = soup.find('span', class_='num').get_text()

print('전체 논문 수 : ' + count_temp)
print()

count_arr = count_temp.split(',')

# 논문 수 (int형변환)
nm_count = ""
for i in count_arr:
    nm_count += i

nm_count = round(int(nm_count) / 10)

# print(nm_count)

# 모든 페이지 논문 크롤링
for n in range(nm_count):
    # for n in range (1):
    url = baseUrl.format(n*10) + plusUrl

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # 전체 논문 수 string형
    for k in range(10):
        # 제목
        title = soup.select('div.cont > p.title > a')[k].text
        # 상세 url
        detail_url = soup.select('div.cont > p.title > a')[k].attrs['href']
        # 저자
        author = soup.select('div.cont > p.etc > span.writer > a')[k].text
        # 대학
        univ = soup.select('div.cont > p.etc > span.assigned > a')[k].text
        # 연도
        year = soup.select('div.cont >  p.etc >  span:nth-child(3)')[k].text
        # 학위
        degree = soup.select('div.cont > p.etc > span:nth-child(4)')[k].text
        # 원문 url
        origin_url = soup.select('div.btnW > ul > li > a')[k].attrs['onclick']

        print('## 목록에서 크롤링한 데이터')
        print('제목 :' + title)
        print('상세 url :' + detail_url)
        print('저자 :' + author)
        print('대학 :' + univ)
        print('연도 :' + year)
        print('학위 :' + degree)
        print('원문 url :' + origin_url)
        print()

        print('## 상세로 들어가서 크롤링한 데이터')
        # print('http://www.riss.kr'+detail_url)
        # print('http://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=8996a952b775390d')
        driver.get('http://www.riss.kr' + detail_url)
        time.sleep(1)

        inner_html = driver.page_source
        inner_soup = BeautifulSoup(inner_html, 'html.parser')
        # print(inner_soup)
        # 제목
        inner_title = inner_soup.select('div.thesisInfoTop > h3.title')[0].text
        # 저자
        inner_author = inner_soup.select('div.infoDetailL > ul > li > div > p > a')[0].text
        # 발행사항
        # inner_fromyear = inner_soup.select('div.infoDetail > ul > li:nth-child(2) > div > p')[0].text
        # # 학위논문사항
        # inner_degreeoption = inner_soup.select('div.infoDetail > ul > li:nth-child(3) > div > p')[0].text
        # # # 발행연도
        # inner_year = inner_soup.select('div.infoDetail > ul > li:nth-child(4) > div > p')[0].text
        # # # 작성언어
        # inner_lang = inner_soup.select('div.infoDetail > ul > li:nth-child(5) > div > p')[0].text
        # # # 주제어
        # inner_keyword = inner_soup.select('div.infoDetail > ul > li:nth-child(6) > div > p')[0].text
        # # # 발행국(도시)
        # inner_city = inner_soup.select('div.infoDetail > ul > li:nth-child(7) > div > p')[0].text
        # # # 형태사항
        # inner_size = inner_soup.select('div.infoDetail > ul > li:nth-child(8) > div > p')[0].text
        # # # 일반주기명
        # inner_general = inner_soup.select('div.infoDetail > ul > li:nth-child(9) > div > p')[0].text
        # # # 소장기관
        # inner_place = inner_soup.select('div.infoDetail > ul > li:nth-child(10) > div > p')[0].text

        print('제목 :' + inner_title.strip())
        print('저자 :' + inner_author.strip())
        # print('발행사항 :' + inner_author)
        # print('학위논문사항 :' + inner_degreeoption)
        # print('발행연도 :' + inner_year)
        # print('작성언어 :' + inner_lang)
        # print('주제어 :' + inner_keyword)
        # print('발행국(도시) :' + inner_city)
        # print('형태사항 :' + inner_size)
        # print('일반주기명 :' + inner_general)
        # print('소장기관 :' + inner_place)
        print()
        # 초록부터는 양이 너무 많아서 일단 제외

        print('-----------------------------------------------------------------------------')

driver.close()

# print를 객체로 전환해 데이터만 만들어주면 됨
# 이름 대학에도 링크가 걸려있던데 이것도 응용하면 어떨지
# 제가 볼때 크롤링 데이터에서 추천이 아니라 이 데이터를 DB에 넣어야할 것 같습니다
# 너무 느립니다. 제 로직 문제인 것 같긴 하지만..
# 크롤링으로 이미지 가져올 수 있는데 논문 이미지 추출과 연관지을 수 있다면 시도해보는 것두...

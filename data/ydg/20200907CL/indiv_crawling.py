import urllib.request
import urllib.parse

from bs4 import BeautifulSoup
import requests

# 논문마다 칼럼이 다 다름. 칼럼이 다 채워진 걸 기준으로 해야하는데 지금 기준 잡은 논문이 최대치인지 확실치 않음
# 목록 크롤링에서 여기 url로 들어올 때 셀레니움 써야할 듯 싶습니다. 저 복호화된 코드가 뭘 의미하는지 정확하지 않아서 대체가 불가능합니다.
# 여기도 정보에 링크 걸려 있어서 응용하려면 응용 가능
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
r=requests.get('http://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=4de583e535e704edffe0bdc3ef48d419', headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


# print(url)
# # 전체 논문 수 string형
# count_temp = soup.find('span', class_='num').get_text()
# 제목
# title = soup.select('div.thesisInfoTop > h3.title').text
# 발행사항
# fromyear = soup.select('div.infoDetail > ul > li ').text
# 학위논문사항
# degreeoption = soup.select('div.thesisInfoTop > h3.title').text
# # 발행연도
# year = soup.select('div.thesisInfoTop > h3.title').text
# # 작성언어
# lang = soup.select('div.thesisInfoTop > h3.title').text
# # 주제어
# keyword = soup.select('div.thesisInfoTop > h3.title').text
# # 발행국(도시)
# city = soup.select('div.thesisInfoTop > h3.title').text
# # 형태사항
# size = soup.select('div.thesisInfoTop > h3.title').text
# # 일반주기명
# general = soup.select('div.thesisInfoTop > h3.title').text
# # 소장기관
# place = soup.select('div.thesisInfoTop > h3.title').text

# print('제목 :' + title)
# print('발행사항 :' + fromyear)
# print('학위논문사항 :' + degreeoption)
# print('발행연도 :' + year)
# print('작성언어 :' + lang)
# print('주제어 :' + keyword)
# print('발행국(도시) :' + city)
# print('형태사항 :' + size)
# print('일반주기명 :' + general)
# print('소장기관 :' + place)

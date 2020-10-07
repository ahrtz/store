import requests
import xml.etree.ElementTree as ET
kor_title = '텍스트마이닝 기법을 활용한 부산시 지역혁신정책 동향분석'

url = "https://open.kci.go.kr/po/openapi/openApiSearch.kci?key=19192000&apiCode=articleSearch&title=" + kor_title
response = requests.get(url=url)
if(response.status_code == 200):
    xml = response.text
tree = ET.ElementTree(ET.fromstring(xml))
root = tree.getroot()
eng_title = root.find('outputData').find('record').find('articleInfo').find('title-group').find('article-title[@lang="english"]').text
print(eng_title)
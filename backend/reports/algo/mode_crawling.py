from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from django.conf import settings
from webdriver_manager.chrome import ChromeDriverManager
# Selenium Setting
def crawling_setting(title_data):
    # try:
        
    # chromedriver = 'chromedriver.exe'
    chromedriver = webdriver.Chrome(ChromeDriverManager().install())
    # print(chromedriver)
    driver = webdriver.Chrome(chromedriver)

    url = "https://www.kci.go.kr/kciportal/po/member/popup/loginForm.kci"
    driver.get(url)
    driver.implicitly_wait(3)

    # 로그인 => 추후에 id, pw 지우기
    login = driver.find_element_by_name("uid")
    login.send_keys("ksb0925")
    login = driver.find_element_by_name("upw")
    login.send_keys("30286450")
    login.send_keys('\n')

    text = driver.find_element_by_id("mainSearchKeyword")
    
    text.send_keys(title_data)

    search = driver.find_element_by_xpath("//button[@class='searchbtn']")
    search.click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    list_data = soup.select('#poArtiSearList table tbody tr td a')[0]['href']
    driver.execute_script(f"window.open('{list_data}')")
    driver.implicitly_wait(2)
    # except:
    #     driver.quit()
    #     return -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1

    while True:
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)

        # Setting
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        if len(soup.select(".articleInfo p span")) > 0:
            break

    # link Scrap
    link_data = driver.current_url

    # title Scrap
    title_data_ko = soup.select(".articleInfo p span")[0].get_text()
    title_data_en = soup.select(".articleInfo p span")[1].get_text()
    title_data_plus1 = int(soup.select(".articleRight div.citation p span")[0].get_text().replace('\n', '').strip().replace("회", ''))
    title_data_plus2 = int(soup.select(".articleRight div.tools p")[0].get_text().replace('\n', '').strip().replace("회 열람", ''))

    # journalInfo Scrap
    journalInfo1 = soup.select(".journalInfo div.overbox p a")[0].get_text().replace('\n', '').strip().replace(' ', '')
    journalInfo2 = soup.select(".journalInfo p.vol a")[0].get_text().replace('\n', '').strip().replace(' ', '')
    journalInfo3 = soup.select(".journalInfo div.overbox p a")[1].get_text().replace('\n', '').strip().replace(' ', '')

    # name Scrap
    name1 = []
    for x in range(len(soup.select(".author a"))):
        name1.append(soup.select(".author a")[x].get_text().replace('\n', '').strip().replace(' ', '')[0:-1])
    name2 = []
    for x in range(len(soup.select(".attach p"))):
        name2.append(soup.select(".attach p")[x].get_text().replace('\n', '').strip().replace(' ', '')[1:])
        
    content1 = soup.select(".articleBody div.box div.innerBox p")[0].get_text().strip()
    content2 = soup.select(".articleBody div.box div.innerBox p")[1].get_text().strip()
    content3 = []
    for x in range(len(soup.select(".articleBody div.box div.innerBox div.overbox a"))):
        if x%3 == 0:
            content3.append(soup.select(".articleBody div.box div.innerBox div.overbox a")[x].get_text().strip())

    content4 = soup.select(".articleBody div.box div.innerBox p")[2].get_text().strip().split(', ')

    reference = []
    for x in range(len(soup.select(".articleBody div.box div.printList p.ref"))):
        temp = soup.select(".articleBody div.box div.printList p.ref")[x].get_text().strip().replace('\n', '').replace('\t', '')
        while True:
            cnt = temp.count('  ')
            if cnt == 0:
                break
            temp = temp.replace('  ', ' ')
        reference.append(temp)

    try:
        driver.quit()
    except:
        pass

    return link_data, title_data_ko, title_data_en, title_data_plus1, title_data_plus2, journalInfo1, journalInfo2, journalInfo3, name1, name2, content1, content2, content3, content4, reference
    '''
    print(link_data)
    print(title_data_ko)
    print(title_data_en)
    print(title_data_plus1)
    print(title_data_plus2)

    print(journalInfo1)
    print(journalInfo2)
    print(journalInfo3)

    print(name1)
    print(name2)

    print(content1)
    print(content2)
    print(content3)
    print(content4)

    print(reference)
    '''
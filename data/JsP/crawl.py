import xlrd
import xlwt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def crawler_thesis_chk_setting():
    """
    kci checkbox setting
    :return:
    """
    
    driver = webdriver.Chrome(ChromeDriverManager().install())

    url = "https://www.kci.go.kr/kciportal/po/member/popup/loginForm.kci"
    driver.get(url)
    driver.implicitly_wait(10)

    # 로그인 => 추후에 id, pw 지우기
    login = driver.find_element_by_name("uid")
    login.send_keys("ahrtzzinn")
    login = driver.find_element_by_name("upw")
    login.send_keys("Kingtop11-")
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

    chk_major = driver.find_element_by_id("majorD")
    chk_major.click()

    for i in range(0, 11):
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

    # excel 다운 클릭
    download_path = "C:/Users/ahrtz/Downloads/"
    for i in range(2, 3):   # range(1, int_last_page) 추후에 모든 페이지 excel로 출력
        driver.execute_script("javascript:goPage("+str(i)+")")
        driver.find_element_by_id("checkAll").click()
        # driver.execute_script("lf_exceldown()")

        # 엑셀 새로 생성
        rb = xlrd.open_workbook(download_path+"논문검색리스트Excel ("+str(i)+").xls")
        rb_sheet = rb.sheet_by_index(0)
        wb = xlwt.Workbook(encoding='utf-8')
        wb_sheet = wb.add_sheet('논문검색리스트', cell_overwrite_ok=True)
        nrows = rb_sheet.nrows
        ncols = rb_sheet.ncols

        for row in range(nrows):
            for col in range(ncols):
                wb_sheet.write(row, col, rb_sheet.cell_value(row, col))
        wb_sheet.write(0, ncols, 'abstract')
        wb_sheet.write(0, ncols+1, 'quotation')

        for j in range(1, 301):   # range(1, 301) 추후에 모든 논문 상세페이지에서 abstract 추출
            detail = driver.find_element_by_xpath("//*[@id='poArtiSearList']/table/tbody/tr["+str(j)+"]/td[2]/p/label/a")
            detail.send_keys('\n')
            abstract = driver.find_element_by_xpath("//*[@id='printArea']/div[2]/div[1]/div/p")
            list_cita = driver.find_element_by_id("listCita")
            list_cnt = list_cita.text.split("는")[1].split("건")[0]
            print(list_cnt)
            # try:
            #     wos_cita = driver.find_element_by_id("wosCitaList")
            #     wos_cnt = wos_cita.find_element('span')
            #     print(wos_cnt.text)
            # except Exception as e:
            #     print(e)

            # print(abstract.text)
            wb_sheet.write(j, ncols, abstract.text)
            wb_sheet.write(j, ncols+1, list_cnt)
            driver.back()
            
        wb.save("논문검색리스트 정제 ("+str(i)+").xls")


if __name__ == '__main__':
    crawler_thesis_chk_setting()
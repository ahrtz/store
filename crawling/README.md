# KCI Crawling

## 🏃 Getting Started

You can start `crawling_kci.py` following these steps:

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a [Windows 10](https://www.microsoft.com/en-us/software-download/windows10) machine
- You have installed the version of [python 3.6.8]()

### Using Crawling_KCI

To use `crawling_kci.py`, follow these steps:

1. Download libraries

   - **Selenium** to connect with the browser

     ```
     $ pip install selenium
     ```

   - **Xlrd** to read .xls files

     ```
     $ pip install xlrd
     ```

   - **Xlwt** for writing .xls files

     ```
     $ pip install xlwt
     ```

2. Run python

   ```
   $ python crawling_kci.py
   ```

### Code

* 다운로드 경로: `download_path = C:\Users\multicampus\Downloads`
* 다운로드 경로 안에 `논문검색리스트Excel.xls`  파일이 미리 있어야 오류가 나지 않습니다.
* 300개씩 `논문검색리스트Excel (index).xls` 파일이 생성됩니다
  * 이 때, `논문검색리스트Excel (index).xls`  파일이 생성되면 (index)페이지의 논문들을 하나씩 상세 조회를 합니다. 상세 조회에서 abstract을 크롤링한 다음 `논문검색리스트 정제 (index).xls` 파일을 새로 생성해 기존 엑셀에 abstract column을 추가해 해당 abstract를 추가해 저장합니다.
  * 총 `int_last_page` 개 만큼 excel이 생성됩니다. 

```python
    # excel 다운 클릭
    download_path = "C:/Users/multicampus/Downloads/"
    for i in range(1, 2):   # range(1, int_last_page) 추후에 모든 페이지 excel로 출력
        driver.execute_script("javascript:goPage("+str(i)+")")
        driver.find_element_by_id("checkAll").click()
        driver.execute_script("lf_exceldown()")

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

        for j in range(1, 5):	# range(1, 301) 추후에 모든 논문 상세페이지에서 abstract 추출
            detail = driver.find_element_by_xpath("//*[@id='poArtiSearList']/table/tbody/tr["+str(j)+"]/td[2]/p/label/a")
            detail.send_keys('\n')
            abstract = driver.find_element_by_xpath("//*[@id='printArea']/div[2]/div[1]/div/p")
            print(abstract.text)
            wb_sheet.write(j, ncols, abstract.text)
            driver.back()
            
        wb.save("논문검색리스트 정제 ("+str(i)+").xls")
```


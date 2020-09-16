#-*- coding: utf-8 -*- 

from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

import pdfplumber

print("텍스트 파일을 추출할 PDF 파일명을 입력하세요.")
PDFfileName = input() + '.pdf'

fp = open(PDFfileName, 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)
temp = ""

cnt = 1
# 01. Page를 나눈다.
for page in pages:
    print("PDF 파일 읽는 중.... " + str(cnt) + " page")
    temp += "======================================================================\n"
    interpreter.process_page(page)
    layout = device.get_result()
    for obj in layout:
        if isinstance(obj,LTTextBox):
           for lobj in obj:
              if isinstance(lobj,LTTextLine):
                    text =  lobj.get_text()
                    temp += text
    
    temp += "\n\n"
    cnt += 1

print("PDF 파일 로드 완료!")
print("")

print("띄어쓰기 교정 중...")
# 02. 띄어쓰기 두번으로 되어있는거 한 번으로 수정하기
while True:
   cnt = temp.count('  ')
   if cnt == 0:
      break

   temp = temp.replace('  ', ' ')
print("띄어쓰기 교정 완료!")

fileOut = open('output.txt', 'w', encoding='utf-8')
print(temp, file=fileOut)
fileOut.close()

with pdfplumber.open(PDFfileName) as pdf:
   first_page = pdf.pages[0]
   print(first_page.extract_table())
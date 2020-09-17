#-*- coding: utf-8 -*- 

from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTTextBoxHorizontal
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import re
import itertools
import collections

def isEnglishOrKorean(input_s):
   k_count = 0
   e_count = 0
   for c in input_s:
      if ord('가') <= ord(c) <= ord('힣'):
         k_count+=1
      elif ord('a') <= ord(c.lower()) <= ord('z'):
         e_count+=1
   return "korean" if k_count > 1 else "english"

# ===============================================================================================
# 00. PDF를 불러온다.
print("텍스트 파일을 추출할 PDF 파일명을 입력하세요.")
PDFfileName = 'documents/' + input() + '.pdf'

fp = open(PDFfileName, 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)


# ===============================================================================================
# 01. Page를 나눈다.
text_list = []
textfont_list = []
cnt = 1

obj_cnt = 0
title_cnt = 0
title_num = 0
title_data = ""

result_test = ""
for page in pages:
   print("PDF 파일 읽는 중.... " + str(cnt) + " page")
   interpreter.process_page(page)
   layout = device.get_result()

   temp = []
   tempfont = []
   for obj in layout:
      if isinstance(obj, LTTextBox):
         for lobj in obj:
            if isinstance(lobj,LTTextLine):
               if cnt == 1 and title_cnt < (lobj.bbox[3] - lobj.bbox[1]):
                  title_cnt = (lobj.bbox[3] - lobj.bbox[1])
                  title_data = obj.get_text()
                  title_num = obj_cnt
               
               temp.append(lobj.get_text())
               tempfont.append(round(lobj.bbox[3] - lobj.bbox[1], 2))
         obj_cnt += 1

   text_list.append(temp)
   textfont_list.append(tempfont)
   cnt += 1
print("PDF 파일 로드 완료!")
print("")


# ===============================================================================================
# 02. 타이틀 헤더 찾고, 교정한다.
title_data = title_data.replace('\n', ' ')
title_data = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", '', title_data)
while True:
   cnt = title_data.count('  ')
   if cnt == 0:
      break
   title_data = title_data.replace('  ',' ')
p = re.compile("[^0-9]")
title_data = "".join(p.findall(title_data))
print("타이틀 : ", title_data, title_num)


# ===============================================================================================
# 03. 띄어쓰기, 맞춤법을 교정한다.
result = ""
print("띄어쓰기, 맞춤법 교정 중...")
for y in range(len(text_list)):
   for x in range(len(text_list[y])):
      temp = text_list[y][x].replace('\n', ' ')
      while True:
         cnt = temp.count('  ')
         if cnt == 0:
            break
         temp = temp.replace('  ',' ')
      text_list[y][x] = temp
print("띄어쓰기 교정 완료!")


# ===============================================================================================
# 04. 가장 많이 쓰는 일반적인 폰트 크기를 알아본다.
textsize_list = list(itertools.chain.from_iterable(textfont_list))
collect = collections.Counter(textsize_list)
collect = collect.most_common()
collect_list = []
collect_data = []
for y in range(len(collect)):
   collect_list.append(collect[y][0])
   collect_data.append("")

for y in range(len(text_list)):
   for x in range(len(text_list[y])):
      for z in range(len(collect_list)):
         if textfont_list[y][x] == collect_list[z]:
            collect_data[z] += text_list[y][x]
            break

collect_max = 0
collect_loc = 0
for z in range(len(collect_list)):
   # print(collect_list[z], len(collect_data[z]))
   if collect_max < len(collect_data[z]):
      collect_max = len(collect_data[z])
      collect_loc = collect_list[z]
print(collect_loc)

for y in range(len(text_list)):
   for x in range(len(text_list[y])):
      if text_list[y][x] != "":
         if x == len(text_list[y])-1:
            result += text_list[y][x] + str(textfont_list[y][x]) + "\n\n"
         else:
            if abs(textfont_list[y][x] - textfont_list[y][x+1]) == 0:
               result += text_list[y][x]
            else:
               result += text_list[y][x] + str(textfont_list[y][x]) + "\n\n"

'''
# ===============================================================================================
# 04-01. 표, 그림 데이터를 걸러낸다.
cnt = 0
figure_list = []
for y in range(len(text_list)):
   for x in range(len(text_list[y])):
      temp = text_list[y][x].strip().split(" ")
      temp1 = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", '', temp[0])
      temp2 = ""
      if len(temp) > 1:
         temp2 = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", '', temp[1])

      if temp1 == '표' or temp1 == 'table' or temp2 == '표' or temp2 == 'table':
         text_list[y][x] = ""
         cnt = 1
      
      if cnt == 1 and abs(collect_loc - textfont_list[y][x]) != 0:
         text_list[y][x] = ""
      elif cnt == 1 and abs(collect_loc - textfont_list[y][x]) == 0:
         cnt = 0

print(figure_list)
'''

fileOut = open('output.txt', 'w', encoding='utf-8')
print(result, file=fileOut)
fileOut.close()
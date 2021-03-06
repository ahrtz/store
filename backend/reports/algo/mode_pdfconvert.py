#-*- coding: utf-8 -*- 

from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTTextBoxHorizontal, LTFigure, LTImage, LTChar, LTLine
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager

import re
import itertools
import collections

import os
from binascii import b2a_hex
from .mode_imageconvert import removeAllFile

# 이미지 저장해주는 함수
def save_image(lt_image, PDFpathName):
    images_folder = 'images/' + PDFpathName
    print(images_folder,'$@#$!')
    print(lt_image)

    """Try to save the image data from this LTImage object, and return the file name, if successful"""
    result = None
    if lt_image.stream:
        file_stream = lt_image.stream.get_rawdata()
        if file_stream:
            file_ext = determine_image_type(file_stream[0:4])
            if file_ext:
                #file_name = ''.join([str(image_index), '_', lt_image.name, file_ext])
                file_name = ''.join([lt_image.name, file_ext])
                if write_file(images_folder, file_name, file_stream, flags='wb'):
                    result = file_name
            else:
                result = lt_image.name + " No Image"
 
    return result

# 이미지 타입 결정해주는 함수
def determine_image_type (stream_first_4_bytes):
    """Find out the image file type based on the magic number comparison of the first 4 (or 2) bytes"""
    file_type = None
    #bytes_as_hex = b2a_hex(stream_first_4_bytes)
    bytes_as_hex = b2a_hex(stream_first_4_bytes).decode(encoding='utf-8')
    # print(bytes_as_hex)
    if bytes_as_hex.startswith('ffd8'):
        file_type = '.jpg'
    elif bytes_as_hex == '89504e47':
        file_type = '.png'
    elif bytes_as_hex == '47494638':
        file_type = '.gif'
    elif bytes_as_hex.startswith('424d'):
        file_type = '.bmp'
    elif bytes_as_hex.startswith('49492a'):
        file_type = '.tif'

    return file_type

# 이미지 저장하는 함수
def write_file (folder, filename, filedata, flags='w'):
    """Write the file data to the folder and filename combination
    (flags: 'w' for write text, 'wb' for write binary, use 'a' instead of 'w' for append)"""
    result = False
    if os.path.isdir(folder):
        try:
            file_obj = open(os.path.join(folder, filename), flags)
            file_obj.write(filedata)
            file_obj.close()
            result = True
        except IOError:
            pass
    return result

# 한글, 영문 판단 해주는 기계
def isEnglishOrKorean(input_s):
   k_count = 0
   e_count = 0
   for c in input_s:
      if ord('가') <= ord(c) <= ord('힣'):
         k_count+=1
      elif ord('a') <= ord(c.lower()) <= ord('z'):
         e_count+=1

   if k_count > 1:
       return "korean"
   elif e_count > 1:
       return "english"
   else:
       return "none"

# PDF 파일을 열게 해주는 함수 (pdfminer 이용)
def pdfopen(PDFfileName):
    try:
        fp = open(PDFfileName, 'rb')
    except:
        return -1, -1, -1

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)

    return device, interpreter, pages

# PDF 파일을 읽어주는 함수 (pdfminer 이용)
def pdfread(device, interpreter, pages, PDFpathName):
    # 이미지 폴더 초기화
    from django.conf import settings

    removeAllFile(str(settings.BASE_DIR / 'images' / PDFpathName))

    text_list = []
    textfont_list = []
    textmiddle_list = []
    textmiddle_average = 0.0
    textfont_average = 0.0
    textfont_cnt = 0

    obj_cnt = 0
    title_cnt = 0

    title_num = 0
    title_data = ""
    cnt = 1
    image_name = []
    image_list = []

    char_list = ""

    for page in pages:
        # print("PDF 파일 읽는 중.... " + str(cnt) + " page")
        interpreter.process_page(page)
        layout = device.get_result()
        temp = []
        tempfont = []
        tempmiddle = []

        for obj in layout:
            # print(obj)
            if isinstance(obj, LTTextBox):
                for lobj in obj:
                    if isinstance(lobj,LTTextLine):
                        if cnt == 1 and title_cnt < (lobj.bbox[3] - lobj.bbox[1]):
                            title_cnt = (lobj.bbox[3] - lobj.bbox[1])
                            title_data = obj.get_text()
                            title_num = obj_cnt
                    
                        temp.append(lobj.get_text())
                        tempfont.append(round(lobj.bbox[3] - lobj.bbox[1], 2))
                        tempmiddle.append(round(lobj.bbox[0], 2))

                        textfont_average += lobj.bbox[0]
                        textfont_cnt += 1
                        if textmiddle_average < (lobj.bbox[2] - lobj.bbox[0]):
                            textmiddle_average = (lobj.bbox[2] - lobj.bbox[0])
                obj_cnt += 1

            if isinstance(obj,LTFigure):
                for ltimages in obj._objs:
                    if isinstance(ltimages, LTImage):
                        PDFpathName1=PDFpathName+'1'
                        result = save_image(ltimages, PDFpathName1)
                        if result:
                            image_name.append(result)
                        else:
                            image_name.append("")
                        image_list.append(cnt)

                    if isinstance(ltimages, LTChar):
                        char_list += ltimages.get_text()

        text_list.append(temp)
        textfont_list.append(tempfont)
        textmiddle_list.append(tempmiddle)
        cnt += 1

    image_temp1 = []
    image_temp2 = []
    for y in range(len(image_name)):
        if image_name[y] != "" and image_name.count(image_name[y]) == 1:
            image_temp1.append(image_name[y])
            image_temp2.append(image_list[y])
            # print(image_name[y], image_list[y])
    image_name = image_temp1
    image_list = image_temp2

    if textfont_cnt > 0:
        textfont_average = int(textfont_average / textfont_cnt)
    else:
        textfont_average = 0

    # print("PDF 파일 로드 완료!")
    # print("")

    return text_list, textfont_list, textmiddle_list, title_num, title_data, image_name, image_list, textmiddle_average/2, textfont_average, char_list

# 논문 Title을 찾고, 특수 문자를 제거해준다.
def title_return(title_data):
    title_data = title_data.replace('\n', ' ')
    title_data = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", '', title_data)

    while True:
        cnt = title_data.count('  ')
        if cnt == 0:
            break
        title_data = title_data.replace('  ',' ')

    p = re.compile("[^0-9]")
    title_data = "".join(p.findall(title_data))
    return title_data

# 띄어쓰기를 교정해주는 함수이다.
def list_return(text_list):
    # print("띄어쓰기 교정 중...")
    for y in range(len(text_list)):
        for x in range(len(text_list[y])):
            temp = text_list[y][x].replace('\n', ' ')
            while True:
                cnt = temp.count('  ')
                if cnt == 0:
                    break
                temp = temp.replace('  ',' ')
            text_list[y][x] = temp
    # print("띄어쓰기 교정 완료!")
    # print("")
    return text_list

# 가장 많이 쓰인 텍스트 사이즈를 반환해준다.
def maxsize_return(text_list, textfont_list):
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
        if collect_max < len(collect_data[z]) and collect_list[z] > 8.50:
            collect_max = len(collect_data[z])
            collect_loc = collect_list[z]
    return collect_loc

# PDF 파일 다단 구분해주기 (pdfminer 이용)
def pdfsort(text_list, textfont_list, textmiddle_list, textmiddle_average, textfont_average):
    text_list2 = []
    textfont_list2 = []
    figure_data = []
    figure_list = []

    for y in range(len(text_list)):
        if len(text_list[y]) > 0:
            temp_list = []
            tempfont_list = []

            refer_location = -1
            refer_text = ""
            refer_font = 0.0

            for x in range(len(text_list[y])):
                if text_list[y][x].count('그림') and text_list[y][x].find('그림') < 3:
                    figure_data.append(text_list[y][x])
                    figure_list.append(y+1)
                elif text_list[y][x].count('Figure') and text_list[y][x].find('Figure') < 3:
                    figure_data.append(text_list[y][x])
                    figure_list.append(y+1)
                elif text_list[y][x].count('Fig') and text_list[y][x].find('Fig') < 3:
                    figure_data.append(text_list[y][x])
                    figure_list.append(y+1)
    
            for x in range(len(text_list[y])):
                if textmiddle_list[y][x] <= 272:
                    # 참고문헌 뒤 삭제
                    temp = text_list[y][x].replace(' ', '')
                    temp = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", '', temp)

                    if temp == '참고문헌' or temp == 'Reference' or temp == 'reference':
                        refer_location = x
                        refer_text = text_list[y][x]
                        refer_font = textfont_list[y][x]
                        break

                    temp_list.append(text_list[y][x])
                    tempfont_list.append(textfont_list[y][x])

            for x in range(len(text_list[y])):
                if refer_location == x:
                    temp_list.append(refer_text)
                    tempfont_list.append(refer_font)

                if textmiddle_list[y][x] > 272:
                    temp_list.append(text_list[y][x])
                    tempfont_list.append(textfont_list[y][x])
            
            text_list2.append(temp_list)
            textfont_list2.append(tempfont_list)

    # print(figure_data)
    figure_name = []
    figure_cnt = []
    for y in range(len(figure_data)):
        figure_name.append("==================================================================================================================================================")
        figure_cnt.append(-1)

    for y in range(len(figure_data)):
        for x in range(1, len(figure_data)+1):
            temp = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", '', figure_data[y]).strip()
            temp = temp.split(' ')

            try:
                if (temp[0] == "그림" and int(temp[1]) == x) or (temp[0] == "Figure" and int(temp[1]) == x) or (temp[0] == "Fig" and int(temp[1]) == x):
                    if len(figure_name[x-1]) > len(figure_data[y]):
                        figure_name[x-1] = figure_data[y]
                        figure_cnt[x-1] = figure_list[y]
                        break
            except:
                pass

    figure_temp1 = []
    figure_temp2 = []
    for y in range(len(figure_name)):
        if figure_name[y] == "==================================================================================================================================================":
            break
        figure_temp1.append(figure_name[y])
        figure_temp2.append(figure_cnt[y])
        # print(figure_name[y], figure_cnt[y])
    figure_name = figure_temp1
    figure_list = figure_temp2

    return text_list2, textfont_list2, figure_name, figure_list

# PDF 파일을 텍스트 사이즈로 묶어주는 함수 (pdfminer 이용)
def pdfgrap(text_list, textfont_list):
    text_list2 = []
    textfont_list2 = []
    for y in range(len(text_list)):
        if len(text_list[y]) > 0:
            text_list2.append(text_list[y][0])
            textfont_list2.append(textfont_list[y][0])

            for x in range(1, len(text_list[y])):
                if textfont_list[y][x-1] == textfont_list[y][x]:
                    text_list2[len(text_list2)-1] += text_list[y][x].strip()
                else:
                    text_list2.append(text_list[y][x].strip())
                    textfont_list2.append(textfont_list[y][x])

    return text_list2, textfont_list2

# PDF를 논문 형식에 맞게 최종적으로 다듬는 함수 (pdfminer 이용)
def pdfcutter(text_list, textfont_list, title_num, collect_loc):
    # 타이틀 앞의 내용 삭제
    text_list2 = []
    textfont_list2 = []

    for y in range(title_num+1, len(text_list)):
        text_list2.append(text_list[y])
        textfont_list2.append(textfont_list[y])
    
    # 참고문헌 뒤 삭제
    text_list = text_list2
    textfont_list = textfont_list2
    text_list2 = []
    textfont_list2 = []
    for y in range(len(text_list)):
        temp = text_list[y].replace(' ', '')
        temp = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", '', temp)

        if temp == '참고문헌' or temp == 'Reference' or temp == 'reference':
            break
        else:
            text_list2.append(text_list[y])
            textfont_list2.append(textfont_list[y])

    # 서론 앞 짜르기
    text_list = text_list2
    textfont_list = textfont_list2
    text_list2 = []
    textfont_list2 = []
    cnt = 0
    for y in range(len(text_list)):
        temp = text_list[y].split(" ")

        if (temp[0].count(".") > 0 and len(text_list[y]) < 10) or cnt == 1:
            text_list2.append(text_list[y])
            textfont_list2.append(textfont_list[y])
            cnt = 1

    # 중간 내용 짜르기
    text_list = text_list2
    textfont_list = textfont_list2
    text_list2 = []
    textfont_list2 = []
    cnt = 0
    for y in range(len(text_list)):
        temp = text_list[y].split(" ")

        if temp[0].count(".") > 0 and isEnglishOrKorean(text_list[y]) != 'none':
            # text_list2.append(text_list[y])
            # textfont_list2.append(textfont_list[y])
            cnt = 0

        elif abs(textfont_list[y] - collect_loc) < 0.1 and isEnglishOrKorean(text_list[y]) != 'none' and cnt == 0:
            text_list2.append(text_list[y].strip())
            textfont_list2.append(textfont_list[y])
            cnt = 1
        
        elif abs(textfont_list[y] - collect_loc) < 0.1 and isEnglishOrKorean(text_list[y]) != 'none' and cnt == 1:
            text_list2[len(text_list2) - 1] += text_list[y].strip()

    return text_list2, textfont_list2
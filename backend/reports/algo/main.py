from .mode_pdfconvert import pdfopen
from .mode_pdfconvert import pdfread
from .mode_pdfconvert import title_return
from .mode_pdfconvert import list_return
from .mode_pdfconvert import maxsize_return
from .mode_pdfconvert import pdfsort
from .mode_pdfconvert import pdfgrap
from .mode_pdfconvert import pdfcutter

from django.conf import settings
from django.conf.urls.static import static

from .mode_summarize import summarize_function
from .mode_summarize import keywords_function
from .mode_summarize import visualize_function
import os
from django.conf import settings

from .hanspell.hanspell import spell_checker

# if __name__ == "__main__":
def getpdf(filename):
    print("텍스트 파일을 추출할 PDF 파일명을 입력하세요.")
    tmp3 = settings.BASE_DIR / 'reports/algo/documents'/filename
    print(tmp3)
    # tmp=os.path.join(settings.BASE_DIR,'\\backend\\reports\\algo\\documents')
    # print(settings.BASE_DIR)
    # tmp2=(os.path.join(tmp,filename))
    # PDFfileName = 'documents/' + input() + '.pdf'
    PDFfileName = settings.MEDIA_URL + filename 
    # print(PDFfileName)

    # PDF를 열고, interpreter, pages 변수를 가져온다.
    device, interpreter, pages = pdfopen(tmp3)
    if device == -1 and interpreter == -1 and pages == -1:
        print("PDF 파일을 잘못 입력했습니다.")
        exit()

    # PDF를 읽고, test_list를 가져오고, title을 가져오고, 띄어쓰기를 교정하며, 가장 많이 사용한 텍스트 크기를 반환한다.
    text_list, textfont_list, textmiddle_list, title_num, title_data = pdfread(device, interpreter, pages)
    title_data = title_return(title_data).strip()
    print("타이틀 : ", title_data)
    print("")
    text_list = list_return(text_list)

    collect_loc = maxsize_return(text_list, textfont_list)
    # print(collect_loc)

    # 다단 나누고, 같은 글자 크기끼리 리스트를 합친다.
    text_list, textfont_list = pdfsort(text_list, textfont_list, textmiddle_list)
    text_list, textfont_list = pdfgrap(text_list, textfont_list)
    text_list, textfont_list = pdfcutter(text_list, textfont_list, title_num, collect_loc)

    # 관련 텍스트를 전부 합친다.
    result = ""
    for y in range(len(text_list)):
        result += text_list[y] + " "
    
    # 맞춤법을 교정한다.
    print("맞춤법 교정 시작!")
    result = result.strip().split(".")
    final_result = ""
    for y in range(len(result)):
        print("맞춤법 교정 중.... " + str(round((y+1) / (len(result)+1) * 100, 2)) + "%")
        if len(result[y]) > 0:
            try:
                temp = spell_checker.check(result[y] + '.')
                final_result += temp.as_dict()['checked']
            except:
                final_result += result[y] + "."
    print("맞춤법 교정 완료!")
    print("")

    # 요약서비스를 이용한다
    summarize_data = summarize_function(final_result)

    print("키워드 추출 시작!")
    summarize_tags = keywords_function(final_result)
    print(summarize_tags)
    # visualize_function(summarize_tags)
    print("키워드 추출 완료!")

    fileOut = open('output1.txt', 'w', encoding='utf-8')
    print(final_result, file=fileOut)
    fileOut.close()

    fileOut = open('output2.txt', 'w', encoding='utf-8')
    print(summarize_data, file=fileOut)
    fileOut.close()
    return final_result,title_data+';^'+summarize_data,summarize_tags




from mode_pdfconvert import pdfopen
from mode_pdfconvert import pdfread
from mode_pdfconvert import title_return
from mode_pdfconvert import list_return
from mode_pdfconvert import maxsize_return
from mode_pdfconvert import pdfsort
from mode_pdfconvert import pdfgrap
from mode_pdfconvert import pdfcutter

from mode_summarize import lexlank_function
from mode_summarize import keywords_function
from mode_summarize import visualize_function

from mode_crawling import crawling_setting

from hanspell import spell_checker

import time
import threading
from multiprocessing import Pool # Pool import하기

def mode_main():
    print("텍스트 파일을 추출할 PDF 파일명을 입력하세요.")
    PDFpathName = input()
    PDFfileName = 'documents/' + PDFpathName + '.pdf'

    # PDF를 열고, interpreter, pages 변수를 가져온다.
    device, interpreter, pages = pdfopen(PDFfileName)
    if device == -1 and interpreter == -1 and pages == -1:
        print("PDF 파일을 잘못 입력했습니다.")
        exit()

    # PDF를 읽고, test_list를 가져오고, title을 가져오고, 띄어쓰기를 교정하며, 가장 많이 사용한 텍스트 크기를 반환한다.
    text_list, textfont_list, textmiddle_list, title_num, title_data, image_name, image_list, textmiddle_average, textfont_average, char_list = pdfread(device, interpreter, pages, PDFpathName)
    title_data = title_return(title_data).strip()
    # print(title_data)

    if len(char_list) > 0:
        # print("논문 형식에 따라, 논문 전체 내용을 요약합니다.")

        # print_result = "논문 내용\n"
        # 맞춤법을 교정한다.
        # print("맞춤법 교정 시작!")
        result = char_list.strip().split(".")
        final_result = ""
        for y in range(len(result)):
            # print("맞춤법 교정 중.... " + str(round((y+1) / (len(result)+1) * 100, 2)) + "%")
            if len(result[y]) > 0:
                try:
                    temp = spell_checker.check(result[y] + '.')
                    final_result += temp.as_dict()['checked']
                    print_result += temp.as_dict()['checked'] + "\n"
                except:
                    final_result += result[y] + "."
                    print_result += result[y] + ".\n"
        # print("맞춤법 교정 완료!")
        # print("")

    else:
        try:
            # KCI 사이트에서 관련 정보를 가져온다.
            # print("PDF 논문 분석 중...")
            link_data, title_data_ko, title_data_en, title_data_plus1, title_data_plus2, journalInfo1, journalInfo2, journalInfo3, name1, name2, content1, content2, content3, content4, reference = crawling_setting(title_data)
            # print("PDF 논문 분석 완료!")
            # print("")
        except:
            link_data = -1
    
        text_list = list_return(text_list)
        collect_loc = maxsize_return(text_list, textfont_list)
        # print(collect_loc)

        # 다단 나누고, 같은 글자 크기끼리 리스트를 합친다.
        text_list, textfont_list, figure_name, figure_list = pdfsort(text_list, textfont_list, textmiddle_list, textmiddle_average, textfont_average)
        text_list, textfont_list = pdfgrap(text_list, textfont_list)
        text_list, textfont_list = pdfcutter(text_list, textfont_list, title_num, collect_loc)

        # 관련 텍스트를 전부 합친다.
        result = ""
        print_result = ""
        for y in range(len(text_list)):
            result += text_list[y] + " "

        if link_data == -1:
            pass
            # print("KCI에 등록되어 있지 않은 논문이거나 사이트 액세스 오류입니다.")
        else:
            # 관련 정보를 추가한다.
            print_result = "링크 : " + link_data + "\n\n"
            print_result += "논문 제목(한글) : " + title_data_ko + "\n\n"
            print_result += "논문 제목(영어) : " + title_data_en + "\n\n"
            print_result += "피인용 횟수 : " + str(title_data_plus1) + "\n\n"
            print_result += "열람 횟수 : " + str(title_data_plus2) + "\n\n"
            print_result += "학술지 : " + journalInfo1 + "\n\n"
            print_result += "논문정보 : " + journalInfo2 + "\n\n"
            print_result += "발행기관 : " + journalInfo3 + "\n\n"
            
            print_result += "저자 정보\n"
            for x in range(len(name1)):
                print_result += str(x) + " : " + name1[x] + " (" + name2[x] + ")\n"
            print_result += "\n"

            print_result += "논문 초록\n"
            print_result += content1 + "\n\n"
            print_result += content2 + "\n\n"

            print_result += "키워드\n"
            if len(content3) == len(content4):
                for x in range(len(content3)):
                    print_result += str(x) + " : " + content3[x] + " (" + content4[x] + ")\n"
            else:
                for x in range(len(content3)):
                    print_result += str(x) + " : " + content3[x] + "\n"
            print_result += "\n"

            if len(reference) > 0:
                print_result += "참고 문헌\n"
                for x in range(len(reference)):
                    print_result += reference[x] + "\n"
                print_result += "\n"

        # 그림 데이터를 정제한다.
        figure_image_name = []
        figure_image_src = []
        if len(figure_name) > 0:
            max_cnt = max(image_list)
            max_list = []
            count_list = []
            for x in range(max_cnt+1):
                max_list.append(image_list.count(x))
                count_list.append(0)

                if x >= 1:
                    max_list[x] += max_list[x-1]
            # print(max_list)
            # print(count_list)

            for x in range(len(figure_name)):
                if (count_list[figure_list[x] - 1] + max_list[figure_list[x] - 1]) < max_list[figure_list[x]]:
                    if image_name[(count_list[figure_list[x] - 1] + max_list[figure_list[x] - 1])].count('No Image') == 0:
                        figure_image_name.append(figure_name[x])
                        figure_image_src.append("images/" + image_name[(count_list[figure_list[x] - 1] + max_list[figure_list[x] - 1])])
                    count_list[figure_list[x] - 1] += 1

            if len(figure_image_name) > 0:
                print_result += "그림\n"
                for x in range(len(figure_image_name)):
                    print_result += figure_image_name[x] + " " + figure_image_src[x] + "\n"
                print_result += "\n"


        print_result += "논문 내용\n"
        # 맞춤법을 교정한다.
        # print("맞춤법 교정 시작!")
        result = result.strip().split(".")
        final_result = ""
        for y in range(len(result)):
            # print("맞춤법 교정 중.... " + str(round((y+1) / (len(result)+1) * 100, 2)) + "%")
            if len(result[y]) > 0:
                try:
                    temp = spell_checker.check(result[y] + '.')
                    final_result += temp.as_dict()['checked']
                    print_result += temp.as_dict()['checked'] + "\n"
                except:
                    final_result += result[y] + ". "
                    print_result += result[y] + ".\n"
        # print("맞춤법 교정 완료!")
        # print("")

    # 요약서비스를 이용한다
    # print("요약 서비스 시작!")
    summarize_data = lexlank_function(final_result)
    summarize_result = "본문 요약 (10줄)\n"
    for x in range(len(summarize_data)):
        summarize_result += summarize_data[x] + "\n\n"
    # print("요약 완료!")
    # print("")

    # print("키워드 추출 시작!")
    summarize_tags = keywords_function(final_result)
    # print(summarize_tags)
    visualize_function(summarize_tags)
    # print("키워드 추출 완료!")
    # print("")

    fileOut = open('outputs/output1_' + PDFpathName +'.txt', 'w', encoding='utf-8')
    print(print_result, file=fileOut)
    fileOut.close()

    fileOut = open('outputs/output2_' + PDFpathName +'.txt', 'w', encoding='utf-8')
    print(summarize_result, file=fileOut)
    fileOut.close()
    print("프로그램 완료! 종료하겠습니다.")
    print("")

def main_crawling():
    thread = threading.Thread(target=mode_main)
    thread.start()

# 멀티 프로세싱 : https://beomi.github.io/2017/07/05/HowToMakeWebCrawler-with-Multiprocess/
# https://medium.com/@keyhyuk.kim/python-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EB%A9%80%ED%8B%B0%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EB%A9%80%ED%8B%B0%EC%8A%A4%EB%A0%88%EB%93%9C%EB%A1%9C-%EC%84%B1%EB%8A%A5-%EC%A5%90%EC%96%B4%EC%A7%9C%EA%B8%B0-a7712bcbaa4
if __name__=='__main__':
    start_time = time.time()

    cnt = 0
    while True:
        if cnt == 3:
            break

        if (time.time() - start_time) > 10:
            main_crawling()
            start_time = time.time()
            cnt += 1
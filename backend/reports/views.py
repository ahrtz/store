from rest_framework import serializers
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.viewsets import ModelViewSet
from .models import Reports,Scraps,Summary_report
from .serializers import ReportsSerializers,ScrapsSerializers,ReportsListSerializers
# ImageSerializer
from reports.algo  import main
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from googletrans import Translator
import os
from django.conf import settings

import subject_classification
import user_based
import requests
import xml.etree.ElementTree as ET

class FileUploadViewSet(ModelViewSet):
    permission_classes = []
    
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializers
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(
                       datafile=self.request.data.get('datafile'),
                       abstract_long='',abstract_short='',
                       key=''
                       )
        abstract_long,abstract_short,key=main.main_crawling(str(self.request.data['datafile']))
        serializer.save(
                       datafile=self.request.data.get('datafile'),
                       abstract_long=abstract_long,abstract_short=abstract_short,
                       key=key
                       )


        # print(self.request.data.get('datafile'))
        # self.request.data.get('datafile') <- 이게 파일 명입니다 위치는 media 폴더 아래에 존재 



@api_view(['GET'])
def reports_list(request):
    paginator = PageNumberPagination()
    reports = Summary_report.objects.all()
    page = paginator.paginate_queryset(reports, request)
    serializer = ReportsListSerializers(page, many=True)
    # 필요한 정보만 시리얼라이저의 필드에서 수정하면 됨
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def reports_detail(request,report_id):
    report = get_object_or_404(Summary_report,id=report_id)
    serializer = ReportsListSerializers(report) 
    return Response(serializer.data)

@api_view(['GET'])  # SCrap 리스트 받아오는 곳
def scrap_list(request):
    # print(request.user.id)
    scraps = Scraps.objects.filter(user_id=request.user.id)
    # get_object_or_404(Scraps, user_id=request.user.id)
    
    serializer = ScrapsSerializers(scraps,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def make_scrap(request,report_id):
    report = get_object_or_404(Summary_report,id=report_id)
    serializer = ScrapsSerializers(data=request.data)
    print(report.title_kor)
    if serializer.is_valid():
        serializer.save(user=request.user,summary=report)
        return Response(serializer.data)
    return HttpResponse(status = 404)

@api_view(['POST'])
def delete_scrap(request,scrap_id):
    scrap = get_object_or_404(Scraps,summary_id=scrap_id)
    scrap.delete()
    return HttpResponse(status=200)



@api_view(['GET'])
def searchtitle(request,keyword): # 제목
    translator=Translator()
    key=translator.translate(keyword,dest='en').text
    paginator = PageNumberPagination()
    report = Summary_report.objects.filter(title_kor__contains=key)
    page = paginator.paginate_queryset(report, request)
    # print(page)
    serializer = ReportsListSerializers(page,many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def searchkeyword(request,keyword):
    translator=Translator()
    key=translator.translate(keyword,dest='en').text
    paginator = PageNumberPagination()
    report = Summary_report.objects.filter(keyword_kor__contains=key) ## 이거 ... 데이터 정제가..
    page = paginator.paginate_queryset(report, request)
    serializer = ReportsListSerializers(page,many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def getimage(request,name):
    path_dir = str(settings.BASE_DIR / 'images'/ name)
    path_dir = path_dir+'1'
    file_list = os.listdir(path_dir)
    # serializer = ImageSerializer(path_dir=path_dir,images_id=file_list)
    # print(path_dir,file_list)
    return Response({'path':path_dir,'img_list':file_list},status=200)

## 요약에서 넘겨주는거 
## abstract 분류 키워드 
@api_view(['GET'])
def recommendation_file(request,title,filename):# 이거 pdf 이름이랑 제목 둘다 넘겨줘야함
    kor_title = title
    print(kor_title)
    try:
        url = "https://open.kci.go.kr/po/openapi/openApiSearch.kci?key=19192000&apiCode=articleSearch&title=" + kor_title
        response = requests.get(url=url)
        if(response.status_code == 200):
            xml = response.text
        tree = ET.ElementTree(ET.fromstring(xml))
        root = tree.getroot()
        eng_title = root.find('outputData').find('record').find('articleInfo').find('title-group').find('article-title[@lang="english"]').text
        print(root)

        print(eng_title)        

        report = Summary_report.objects.filter(title_kor=eng_title)
        # print(report.values())
        abstract = report[0].abstract
        subject = report[0].subject
        keyword=report[0].keyword_kor   
    except:
        output2_name='summarize_'+filename +'.txt'
        fileIn = open(settings.BASE_DIR / 'reports/algo/outputs'/ output2_name, 'rt', encoding='utf-8')
        abstract = fileIn.read()
        fileIn.close()

        output3_name='tag_'+filename +'.txt'
        fileIn = open(settings.BASE_DIR / 'reports/algo/outputs'/ output3_name, 'rt', encoding='utf-8')
        key = fileIn.read()
        fileIn.close()
        keyword = []
        tmp=list(key.split("'"))
        # print(tmp)
        for i in range(10):
            keyword.append(tmp[2*i+1])
        subject=''
    # print(abstract,keyword)
    result_idx,result_title,result_keyword=subject_classification.recommend(abstract,[subject],keywords=keyword)  # abstract 분류 키워드 
    # print(result)
    res=[]
    for i in range(5):
        temp=[]
        temp.append(result_idx[i])
        temp.append(result_title[i])
        temp.append(result_keyword[i])
        res.append(temp)
    print(res)

    ## 영어 타이틀 읽어와서 db 검색 잇으면 그거 쓰기 
    ## 없으면 요약본 쓰기 
    return  Response({'result':res},status=200)

## 검색쪽 (우리 디비,)
## 제목 ,분류 
@api_view(['GET'])
def recommendation_db(request,title):#제목
    try:
        result_idx,result_title,result_keyword=user_based.get_item_based_collabor(title)
        res=[]
        for i in range(5):
            temp=[]
            temp.append(result_idx[i])
            temp.append(result_title[i])
            temp.append(result_keyword[i])
            res.append(temp)

        return Response({'result':res},status=200)
    except:
        return Response({'message':'아직 데이터가 모자라요'},status=200)

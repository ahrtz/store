from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.viewsets import ModelViewSet
from .models import Reports,Scraps,Summary_report
from .serializers import ReportsSerializers,ScrapsSerializers,ReportsListSerializers
from reports.algo  import main
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from googletrans import Translator


class FileUploadViewSet(ModelViewSet):
    permission_classes = []
    
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializers
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def perform_create(self, serializer):
        serializer.save(
                       datafile=self.request.data.get('datafile'),
                       abstract_long='',abstract_short='',
                       key=''
                       )
        abstract_long,abstract_short,key=main.getpdf(str(self.request.data['datafile']))
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
    scraps = get_object_or_404(Scraps, user=request.user)
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

@api_view(['GET'])
def searchtitle(request,keyword): # 제목
    translator=Translator()
    key=translator.translate(keyword,dest='en').text
    paginator = PageNumberPagination()
    report = Summary_report.objects.filter(title_eng__contains=key)
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
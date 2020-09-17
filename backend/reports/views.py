from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .models import Reports
from .serializers import ReportsSerializers
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from reports.algo  import main
from rest_framework.response import Response

class FileUploadViewSet(ModelViewSet):
    permission_classes = []
    
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializers
    parser_classes = (MultiPartParser, FormParser,)

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

# @api_view(['GET'])
# def reports_list(request):
#     paginator = PageNumberPagination()
#     reports = Reports.objects.all()
#     page = paginator.paginate_queryset(reports, request)
#     serializer = ReportsListSerializers(page, many=True)
#     return paginator.get_paginated_response(serializer.data)

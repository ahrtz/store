from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .models import Reports
from .serializers import ReportsSerializers


class FileUploadViewSet(ModelViewSet):
    permission_classes = []
    
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializers
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(
                       datafile=self.request.data.get('datafile'))
        # print(self.request.data.get('datafile'))
        # self.request.data.get('datafile') <- 이게 파일 명입니다 위치는 media 폴더 아래에 존재 
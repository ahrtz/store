from rest_framework import serializers
from .models import Reports,Scraps,Summary_report


# 논문 목록
class ReportsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Summary_report
        fields= '__all__'
        # fields = ['id', 'title_kor', 'title_eng', 'main_author', 'sub_author', 'issue_year', 'subject', 'keyword_kor', 'abstract']

# 파일 상세 정보
class ReportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'

class ScrapsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Scraps
        fields='__all__'
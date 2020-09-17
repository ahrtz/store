from rest_framework import serializers
from .models import Reports


# 논문 목록
class ReportsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['id', 'title_kor', 'title_eng', 'main_author', 'sub_author', 'issue_year', 'subject', 'keyword_kor', 'abstract']

# 논문 상세 정보
class ReportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'


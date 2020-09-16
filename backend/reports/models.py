from django.db import models

class Reports(models.Model):# 파일 업로드 용
    datafile = models.FileField()

# class Summary_report(models.Model): # 우리가 정제한 데이터 
#     title_kor = models.CharField(max_length = 300)
#     title_eng = models.CharField(max_length = 300)
#     main_author = models.CharField(max_length = 100) 
#     sub_author = models.TextField() #<- 이거 여러명 클릭 가능한 형식으로 할거면...... 연관 테이블...? 이건 아니엇던듯? 
#     # 저널 이름 
#     journal_kor = models.CharField(max_length = 100)
#     journal_eng = models.CharField(max_length = 100)
#     #발행기관
#     issuer_kor = models.CharField(max_length=100)
#     issuer_eng = models.CharField(max_length=100)
#     issue_year = models.IntegerField()
#     # keyword_kor = 이거 다대다로 엮어야 하는데...? 
#     # keyword_eng = 영어 다대다도 엮어야..? 테이블 한개더..? 
#     subject = models.CharField(max_length = 50)
#     direct_urls = models.URLField(max_length=200) # 200이면 되려나
#     doi = models.CharField(max_length = 50)
#     abstract  = models.TextField() # 이건 요약 정보
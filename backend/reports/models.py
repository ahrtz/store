from django.db import models

class Reports(models.Model):# 파일 업로드 용
    datafile = models.FileField()
    abstract_long= models.TextField(default=None)
    abstract_short=models.TextField(default=None)
    key=models.TextField(default=None)

class Summary_report(models.Model): # 우리가 정제한 데이터 
    title_kor = models.CharField(max_length = 300)
    title_eng = models.CharField(max_length = 300,blank=True)
    main_author = models.CharField(max_length = 100) 
    sub_author = models.TextField() 
    # 저널 이름 
    journal_kor = models.CharField(max_length = 100)
    journal_eng = models.CharField(max_length = 100)
    #발행기관
    issuer_kor = models.CharField(max_length=100)
    issuer_eng = models.CharField(max_length=100)
    issue_year = models.IntegerField(default=0)
    book_num = models.CharField(max_length = 100)
    keyword_kor = models.TextField()
    keyword_eng =  models.TextField()
    subject = models.CharField(max_length = 50)
    quote = models.IntegerField(default=0)
    direct_urls = models.URLField(max_length=200) # 200이면 되려나
    doi = models.CharField(max_length = 50)
    abstract  = models.TextField() # 이건 요약 정보
    page_num=models.CharField(max_length = 100)
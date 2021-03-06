from django.db import models
from django.conf import settings

class Reports(models.Model):# 파일 업로드 용
    datafile = models.FileField()
    abstract_long= models.TextField(default=None)
    abstract_short=models.TextField(default=None)
    key=models.TextField(default=None)

class Summary_report(models.Model): # 우리가 정제한 데이터 
    title_kor = models.CharField(max_length = 300)
    title_eng = models.CharField(max_length = 300,blank=True)
    main_author = models.CharField(max_length = 100) 
    sub_author = models.TextField(blank=True,null=True) 
    # 저널 이름 
    journal_kor = models.CharField(max_length = 100,blank=True,null=True)
    journal_eng = models.CharField(max_length = 100,blank=True,null=True)
    #발행기관
    issuer_kor = models.CharField(max_length=100,blank=True,null=True)
    issuer_eng = models.CharField(max_length=100,blank=True,null=True)
    issue_year = models.IntegerField(default=0,blank=True,null=True)
    book_num = models.CharField(max_length = 100,blank=True,null=True)
    keyword_kor = models.TextField(blank=True,null=True)
    keyword_eng =  models.TextField(blank=True,null=True)
    subject = models.CharField(max_length = 50,blank=True,null=True)
    quote = models.IntegerField(default=0,blank=True,null=True)
    direct_urls = models.URLField(max_length=200,blank=True,null=True) # 200이면 되려나
    doi = models.CharField(max_length = 50,blank=True,null=True)
    abstract  = models.TextField(blank=True,null=True) # 이건 요약 정보
    page_num=models.CharField(max_length = 100,blank=True,null=True)


class Scraps(models.Model):
    summary = models.ForeignKey(Summary_report,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

from django.db import models

class Reports(models.Model):
    report_file = models.FileField()
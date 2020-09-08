from django.db import models

class Reports(models.Model):
    datafile = models.FileField()
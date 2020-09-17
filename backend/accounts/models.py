from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Favorites(models.Model):
    main_category = models.CharField(max_length=100)    # 대분류
    sub_category = models.CharField(max_length=50)  # 소분류
class User(AbstractUser):
    favor = models.ManyToManyField(Favorites,related_name='favorites_user')
    pass


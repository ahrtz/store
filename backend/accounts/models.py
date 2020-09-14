from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Favorites(models.Model):
    content = models.CharField(max_length=255)
class User(AbstractUser):
    favor = models.ManyToManyField(Favorites,related_name='favorites_user')
    pass

    
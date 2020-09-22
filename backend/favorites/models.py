from django.db import models
from django.conf import settings
from accounts.models import User

# Create your models here.
class Favorites(models.Model):
    main_category = models.CharField(max_length=100)    # 대분류
    sub_category = models.CharField(max_length=50)  # 소분류

class User_Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorites =  models.ForeignKey(Favorites, on_delete=models.CASCADE, null=True)
    ranking = models.IntegerField(default=1)
    # first_favorites = models.ForeignKey(Favorites, related_name='related_first_favorites', on_delete=models.CASCADE)
    # second_favorites = models.ForeignKey(Favorites, related_name='related_second_favorites', null=True, on_delete=models.CASCADE)
    # third_favorites = models.ForeignKey(Favorites, related_name='related_third_favorites', null=True, on_delete=models.CASCADE)
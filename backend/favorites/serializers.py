from rest_framework import serializers
from .models import Favorites, User_Favorites
from accounts.serializers import UserSerializer
from django.conf import settings

User = settings.AUTH_USER_MODEL
# 분류 상세 정보
class FavoritesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'

class UserFavoritesSerializers(serializers.ModelSerializer):
    class Meta:
        model = User_Favorites
        fields = '__all__'
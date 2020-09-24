from django.shortcuts import render,get_object_or_404
from .models import Favorites, User_Favorites
from .serializers import FavoritesSerializers, UserFavoritesSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from django.http import HttpResponse
from accounts.models import User

# Create your views here.
@api_view(['GET'])
def favorites_list(request):
    favorites = Favorites.objects.all()
    serializer = FavoritesSerializers(favorites, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def insert_favorites(request):
    favorites = request.data.get('favorites')
    for idx in range(0, len(favorites)):
        serializer = UserFavoritesSerializers(data=favorites[idx])
        if serializer.is_valid():
            favorite = get_object_or_404(Favorites, id=favorites[idx]['favorites_id'])
            serializer.save(favorites=favorite, user=request.user)
    return Response(request.data)

@api_view(['GET'])
def search_favorites(request):
    user_favorites = User_Favorites.objects.filter(user_id=request.user.id)
    serializer = UserFavoritesSerializers(user_favorites, many=True)
    return Response(serializer.data)

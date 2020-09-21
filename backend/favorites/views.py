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
    user = request.user
    user_obj = get_object_or_404(User, username=request.user)
    print(user_obj['id'])

    first_favorites = get_object_or_404(Favorites, id=request.data.get('first_favorites_id'))
    second_favorites = get_object_or_404(Favorites, id=request.data.get('second_favorites_id'))
    third_favorites = get_object_or_404(Favorites, id=request.data.get('third_favorites_id'))
    print(request.data)

    serializer = UserFavoritesSerializers(first_favorites=first_favorites,
                second_favorites=second_favorites, third_favorites=third_favorites)
    # print(serializer)
    
    if serializer.is_valid():
        print('hi')
        serializer.save(user_id=user_obj.id, first_favorites=first_favorites,
                second_favorites=second_favorites, third_favorites=third_favorites)

    return Response(serializer.data)
    
@api_view(['GET'])
def search_favorites(request):
    user = request.user.id
    print(user)
    favorites = User_Favorites.objects.filter(user_id=request.user.id)
    print(favorites)
    serializer = FavoritesSerializers(favorites, many=True)
    return Response(serializer.data)
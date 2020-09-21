from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'addreport',views.FileUploadViewSet,basename='testing')

app_name = 'reports'

urlpatterns = [
    path("",include(router.urls)),
    path('scrap/list/',views.scrap_list),
    path('scrap/make/',views.make_scrap)
]  
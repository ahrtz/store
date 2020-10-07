from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'addreport',views.FileUploadViewSet,basename='testing')

app_name = 'reports'

urlpatterns = [
    path("",include(router.urls)),
    path('scrap/list/',views.scrap_list),
    path('scrap/make/<int:report_id>',views.make_scrap),
    path('scrap/delete/<int:scrap_id>',views.delete_scrap),
    path('list/',views.reports_list),
    path('detail/<int:report_id>',views.reports_detail),
    path('searcht/<str:keyword>/',views.searchtitle),
    path('searchk/<str:keyword>/',views.searchkeyword),
    path('images/<str:name>/',views.getimage),

    path('recommend/<str:title>/<str:filename>',views.recommendation_file),
    path('recommend_search/<str:title>',views.recommendation_db)
]  
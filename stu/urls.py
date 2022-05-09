from django.urls import path
from .api import StuCreateApi,StuApi,StuUpdateApi,StuDeleteApi,StuFindApi
urlpatterns = [
   path('st',StuApi.as_view()),
    path('api/create',StuCreateApi.as_view()),
    path('update/<int:pk>',StuUpdateApi.as_view()),
    path('ap/<int:pk>',StuDeleteApi.as_view()),
    path('a/<int:pk>',StuFindApi.as_view()),
   
]
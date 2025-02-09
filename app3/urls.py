from django.urls import path
from .views import index,about,test

urlpatterns = [
    path('',index,name='app3_index'),
    path('about',about,name='app3_about'),
    path('test',test,name='app3_test'),
]
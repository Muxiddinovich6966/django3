from django.urls import path
from .views import index,about,test
urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('test',test,name='test')
]
from django.urls import path
from .views import index,about,test

urlpatterns = [
    path('',index,name='app2_index'),
    path('about',about,name='app2_about'),
    path('test',test,name='app2_test'),
]
from django.urls import path, re_path  # re_path用来进行正则匹配
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
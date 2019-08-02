from django.urls import path, re_path  # re_path用来进行正则匹配
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^post/(?P<pk>[0-9]+)/$', views.details, name='detail'),
    path('post/<int:pk>', views.details, name='detail'),
    path('post/<int:pk>/', views.details, name='detail'),
    # 以上两种用法，re_path为django1.x版本中url用法，
    # path为django2.2参考文档中用法
]

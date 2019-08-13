from django.urls import path, re_path  # re_path用来进行正则匹配
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^post/(?P<pk>[0-9]+)/$', views.details, name='detail'),
    path('<int:pk>', views.details, name='detail'),
    # 以上两种用法，re_path为django1.x版本中url用法，
    # path为django2.2参考文档中用法,<int:pk>可以理解为贪婪匹配，匹配所有符合的位数的整数
    re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})', views.archives, name='archive'),
    path('category/<int:pk>', views.category, name='category'),
]

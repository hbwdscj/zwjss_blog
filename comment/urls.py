from django.urls import path, re_path
from . import views

app_name = 'comment'
urlpatterns = [
    path('comment/post/<int:post_pk>', views.get_comment, name='post_comment'),
]
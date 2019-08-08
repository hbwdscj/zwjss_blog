from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    url = models.URLField(blank=True)
    created_time = models.DateTimeField(auto_now=True)
    text = models.TextField()
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE,)

    # TODO:此处加入author报1054错误，找不到author_id在数据库中，待解决
    # author = models.ForeignKey(xxxx)

    def __str__(self):
        return self.text[:25]
# Create your models here.

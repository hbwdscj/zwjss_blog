from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Tag, Post


def index(request):
    post_first_list = Post.objects.all().order_by('-created_time')
    post_end_list = [post.title for post in post_first_list]
    context = {
        'post_list': post_end_list,
    }
    return render(request, 'blog/index.html', context=context)

# Create your views here.

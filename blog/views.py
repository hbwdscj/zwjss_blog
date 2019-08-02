from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Tag, Post


def index(request):
    post_list = Post.objects.order_by('-created_time')
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context=context)


def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context=context)

# Create your views here.

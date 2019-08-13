from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Tag, Post
from comment.models import Comment
from comment.forms import CommentForm

def index(request):
    post_list = Post.objects.order_by('-created_time')
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context=context)

def aboutme(request):
    return render(request, 'about.html')

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    post_comment_list = post.comment_set.all()
    post.increase_views()  # 调用models中定义的方法
    context = {
        'post': post,
        'form': form,
        'post_comment_list': post_comment_list
    }
    return render(request, 'blog/detail.html', context=context)


# 根据年份和月份来显示归档时间目录下的文章
def archives(request, year, month):
    """
    此处为解决存在month无法匹配的问题，将settings中的USE_TZ置为False解决。
    在blog——tags中定义了get_archives方法，因此直接在模板中可以获取models的数据，
    此函数未被调用，但是输入url获取时会调用，下同。
    """
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by('-created_time')
    context = {
        'post_list': post_list
        # 因为此处借用了已经渲染了的index.html，index中定义了参数为post_list,因此此处必须遵守
    }
    return render(request, 'blog/index.html', context=context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context=context)
# Create your views here.

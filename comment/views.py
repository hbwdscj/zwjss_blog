from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from blog.models import Post


def get_comment(request, post_pk):

    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            """
            redirect 可以接受一个url或者一个模型实例做为重定向的对象
            当模型做对象时必须在models里面实现get_absolute_url，否则会报noiterable错
            """
            return redirect(post)
        else:
            """
            1.post_comment_list 是一篇post对应的所有评论，因为post和comment是一对多的外键关系，
            post.comment_set.all()用法为少数方对应的所有多数方
            2.else情况为非POST方法的情况：即没有提交数据，因此重定向到重新渲染了的文章详情页，显示已有的数据。
            """
            post_comment_list = post.comment_set.all()
            context = {
                'post_comment_list': post_comment_list,
                'post': post,
                'form': form,
            }
            return render(request, 'blog/detail.html', context=context)
# Create your views here.

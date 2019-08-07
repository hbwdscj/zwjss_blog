# 自定义模板标签在模板中调用
"""
首先导入template模块，然手实例化template.Library类，将函数装饰为register.simple_tag,这样就可以在模板中调用
类似{% get_recent_posts %}函数了
"""
from ..models import Post, Category
from django import template

register = template.Library()


@register.simple_tag  # 对应侧边栏的 最新文章
def get_recent_posts(num=5):
    return Post.objects.order_by('-created_time')[:num]


@register.simple_tag  # 对应侧边栏的 归档
def get_archives():
    return Post.objects.dates('created_time', 'month', order='DESC')
# dates 方法会返回一个列表，元素为每一篇文章的created_time，且是python对象，精确到月份，将序排列，实现按月归档额功能.


@register.simple_tag  # 对应侧边栏的分类
def get_categories():
    return Category.objects.all()


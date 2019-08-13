from ..models import Comment
from django.db.models.aggregates import Count
from django import template

register = template.Library()


@register.simple_tag
def get_comments():
    return Comment.objects.annotate(num_coms=Count('post'))


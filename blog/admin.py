from django.contrib import admin
from .models import Category, Post, Tag, User


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'modified_time', 'category', 'author',]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

# Register your models here.

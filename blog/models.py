from django.db import models
from django.utils import timezone
#         HINT: It seems you set a fixed date / time / datetime value as default for this field.
#         This may not be what you want.
#         If you want to have the current date as default, use `django.utils.timezone.now`
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """
    Blog文章的分类
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        # verbose_name = '分类'
        # verbose_name_plural如果未定义，则在admin界面显示为"分类s"
        verbose_name_plural = '分类'


class Tag(models.Model):
    """
    Blog文章的标签
    """
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Blog文章的主体
    """

    class Meta:
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 文章标题
    title = models.CharField(max_length=50)
    body = models.TextField()
    # 文章创建时间
    created_time = models.DateTimeField(auto_now=True)
    # 文章最后一次修改时间

    modified_time = models.DateTimeField()
    # 文章摘要，此处注意，教程中写CharField默认不能为空，需要设置blank=True，但是看django2.2版本的文档，CharField只有一个额外
    # 属性，即：max_length，此处存疑
    excerpt = models.CharField(max_length=50, blank=True, verbose_name='zhaiyao')
    # 此 处定义文章的分类和标签，前面已经定义了CATEGORY和TAG类
    # 设定：一篇文章只能有一个分类，而一个分类可以有多篇文章，因此采用外键，连接到Category类
    # 设定：一篇文章可以有多个标签，而一个标签可以有多篇文章因此采用ManyToMany，连接到Tag类，并且允许为空，定义blank=True
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name="+")
    # related_name = "+"意在避免多对多表产生后向影响
    # 同category的设定
    author = models.ForeignKey(User, on_delete=models.CASCADE, )

# Create your models here.

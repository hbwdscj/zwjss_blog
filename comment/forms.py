from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    选择forms.ModelsForm还是forms.Form
    如果您正在构建一个数据库驱动的应用程序，那么您很有可能会用到与Django模型密切相关的表单。例如，您可能有一个 BlogComment 模型，
    并且您想创建一个让用户提交评论的表单。在这种情况下，在表单中定义字段类型是多余的，因为您已经在模型中定义了字段。
    """
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text',]

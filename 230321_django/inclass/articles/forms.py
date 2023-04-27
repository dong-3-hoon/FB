from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     # 브라우저에서 보여주는 역할이므로 길이가 필요없어서 필수는 아님 - 맞춰주면 편함
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


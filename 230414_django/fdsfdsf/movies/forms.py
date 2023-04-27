from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('movie_id', 'user_id',)
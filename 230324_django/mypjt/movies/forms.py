from django import forms
from .models import Movie
# class ArticleForm(forms.Form):
#     # 브라우저에서 보여주는 역할이므로 길이가 필요없어서 필수는 아님 - 맞춰주면 편함
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)
class DateInput(forms.DateInput):
    input_type = 'date'

class MovieForm(forms.ModelForm):
    genre_choices = [('코미디','코미디'),('공포','공포'),('로맨스','로맨스')]
    genre = forms.ChoiceField(choices = genre_choices, required = True)
    score = forms.FloatField(max_value=5,min_value=0, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "0.5"}))
    release_data = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Movie
        fields = '__all__'

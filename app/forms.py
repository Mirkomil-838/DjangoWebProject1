"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class RewievsForm(forms.Form):

    name=forms.CharField(label='Ваше имя',min_length=2,max_length=100)
    opinion=forms.ChoiceField(label='Довольны ли вы содержимым сайта?',
                               choices=[('1','Да'),('2','Наверное'),
                                        ('3','Скорее нет'),('4','Нет')],
                               widget=forms.RadioSelect,initial=1)

    preposition=forms.ChoiceField(label='Кому возрасту будет полезен сайт?',
                                  choices=(('1','8-14'),('2','14-18'),
                                           ('3','18-25'),('4','25-40'),('5','40+')),
                                  initial=1)
    flag=forms.BooleanField(label='Хотите получить ответ от нас?',
                            required=False)
    email=forms.EmailField(label='Ваш email: ')
    
    positive=forms.CharField(label='Что вам понравилось больше всего?',
                              widget=forms.Textarea(attrs={'rows':5,'cols':40}))
    negative=forms.CharField(label='Что вам не понравилось больше всего?',
                              widget=forms.Textarea(attrs={'rows':5,'cols':40}))

class CommentForm (forms.ModelForm):

    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):

    class Meta:
        model = Blog # используемая модель
        fields = ('image' ,'author','title','description','content','posted','video','video_1','video_2','imagevideo','imagevideo_1','imagevideo_2') # требуется заполнить только поле text
        labels = {'image':'Изображение' ,'author':'Автор', 'title':'Заголовок', 'description':'Краткое описание', 'content':'Содержание', 'posted':'Дата', 'video':'Видео 1','video_1':'Видео 2','video_2':'Видео 3','imagevideo':'Постер к Видео 1','imagevideo_1':'Постер к Видео 2','imagevideo_2':'Постер к Видео 3'} # метка к полю формы text
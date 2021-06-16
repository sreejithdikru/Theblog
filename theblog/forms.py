from django import forms
from django.forms import fields, models, widgets
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body','upload_img')

        widgets = {

            'title' : forms.TextInput(attrs= {'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs= {'class': 'form-control'}),
            'author' : forms.TextInput(attrs= {'class': 'form-control', 'value' : '', 'id':'writer', 'type' : 'hidden'}),
            #'author' : forms.Select(attrs= {'class': 'form-control'}),
            'body' : forms.Textarea(attrs= {'class': 'form-control'}),
            'upload_img' : forms.FileInput(attrs= {'class': 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {

            'title' : forms.TextInput(attrs= {'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs= {'class': 'form-control'}),
            'body' : forms.Textarea(attrs= {'class': 'form-control'}),

        }


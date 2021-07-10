from django import forms
from django.forms import fields
from .models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','context']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','id':'formGroupExampleInput','placeholder':'Title'}),
            'context':forms.Textarea(attrs={'class':'form-control','id':'formGroupExampleInput2','placeholder':'Context'})

        }
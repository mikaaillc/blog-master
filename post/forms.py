from django import forms
from .models import post,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model=post
        fields=['baslik',
                'metin',
                'image',

               ]



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name',
                'yorum'
        ]
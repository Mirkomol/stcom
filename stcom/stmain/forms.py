from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'status', 'content']




#
# class ProfileSearchForm(forms.Form):
#     name = forms.CharField(required=False)
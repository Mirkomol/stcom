from .models import DormPost
from django import forms


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = DormPost
        fields = ('title', 'image', 'caption','address','phone_number')


from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('title', 'text','img_url','img_alt',)
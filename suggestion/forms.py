from django import forms

from .models import Post,Reply

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ( 'user', 'recipient', 'title', 'text')

class PostReply(forms.ModelForm):
	
    class Meta:
        model = Reply
        fields = ('text', )

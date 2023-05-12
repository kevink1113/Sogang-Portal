from django import forms
from .models import Comment, Post, PostsUser


class NicknameForm(forms.ModelForm):
    class Meta:
        model = PostsUser
        fields = ['nickname']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

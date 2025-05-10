from django import forms
from .models import Comment
from .models import Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'content']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш комментарий', 'rows': 3}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'file']
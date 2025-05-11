from django import forms
from .models import Comment
from .models import Post
from .models import Author
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


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        labels = {'name': 'Имя автора'}

    def clean_name(self):
        name = self.cleaned_data['name']
        if Author.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("Этот автор уже существует!")
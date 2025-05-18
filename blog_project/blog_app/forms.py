from .models import Comment
from .models import Post
from .models import Author
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
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
        fields = ['user', 'bio', 'birth_date', 'website']
        labels = {'bio': 'Био автора', 'birth_date': 'Дата рождения', 'website': 'Сайт автора'}
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
        }

    def clean_name(self):
        name = self.cleaned_data['user']
        if Author.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("Этот автор уже существует!")
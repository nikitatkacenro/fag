from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .forms import CommentForm
from .models import Post, Comment, Like
from .models import Author
from .forms import AuthorForm
from .forms import RegisterForm
import random
from django.shortcuts import render, redirect
from .forms import AuthorChoiceForm

def author_choice(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = AuthorChoiceForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['want_author']

            if choice == 'yes':
                # Шанс 50% стать автором
                if random.random() < 0.5:
                    request.user.is_author = True
                    request.user.save()
                    message = "🎉 Поздравляем! Теперь вы Автор!"
                else:
                    message = "😢 Увы, не повезло. Попробуйте в другой раз!"
            else:
                message = "Вы отказались от шанса стать автором."

            return render(request, 'registration/author_result.html', {'message': message})
    else:
        form = AuthorChoiceForm()

    return render(request, 'registration/author_choice.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('author_choice')
    else:
        form = RegisterForm()
    return render(request, 'blog_app/register.html', {'form': form})
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form=CommentForm()
    return render(request, 'blog_app/post_detail.html', {'post': post})


def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('post_detail', post_id=post.id)


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.get_or_create(user=request.user, post=post)
    return redirect('post_detail', post_id=post_id)


def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    Like.objects.create(comment=comment)
    return JsonResponse({'likes': comment.likes.count()})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog_app/create_post.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()
    return render(request, 'blog_app/add_author.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        author_name = request.POST.get('author')
        author, created = Author.objects.get_or_create(
            name=author_name.strip(),
            defaults={'name': author_name}
        )
        if not created:
            pass
    return render(...)

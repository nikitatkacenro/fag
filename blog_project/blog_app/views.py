from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import AuthorForm
from .forms import CommentForm
from .forms import PostForm
from .forms import RegisterForm
from .models import Author
from .models import Post, Comment, Like


@login_required
def make_author(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        if author := Author.objects.filter(user=user).first():
            return render(request, 'blog_app/author_created.html', {'author': author, 'created': False})
        else:
            author = Author.objects.create(
                user=user
            )
            return render(request, 'blog_app/author_created.html', {'author': author, "created": True})
    else:
        return render(request, 'blog_app/author_choice.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('author_choice')
    else:
        form = RegisterForm()
    return render(request, 'blog_app/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'blog_app/logout.html')


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

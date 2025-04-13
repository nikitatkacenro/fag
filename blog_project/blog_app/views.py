from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Post, Comment, Like

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
    Like.objects.create(post=post)
    return JsonResponse({'likes': post.likes.count()})

def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    Like.objects.create(comment=comment)
    return JsonResponse({'likes': comment.likes.count()})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

from django.contrib import admin
from .models import Post, Comment, Like
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['bio']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ('title','content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','user','created_at')
    search_fields = ('user','content')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post','created_at')
    search_fields = ('post',)

from django.contrib import admin
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ('title','content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author','created_at')
    search_fields = ('author','content')


@admin.register(Like)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','comment','created_at')
    search_fields = ('post','comment')


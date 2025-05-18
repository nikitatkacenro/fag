from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:post_id>/',views.post_detail,name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog_app/logout.html'), name='logout'),
]

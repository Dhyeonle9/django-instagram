from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/likes/', views.likes, name='likes'),
    path('<int:id>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:id>/likes-async/', views.likes_async, name='likes-async'),
]
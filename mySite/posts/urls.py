from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list_view , name='list'),
    path('post_new', views.post_new_view, name='new-post'),
    path('<slug:slug>', views.post_view, name='post'),
]

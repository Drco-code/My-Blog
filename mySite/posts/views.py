from django.shortcuts import render
from .models import Posts
from . import forms

# Create your views here.

def posts_list_view(request):
    posts = Posts.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})


def post_view(request, slug):
    post = Posts.objects.get(slug=slug)
    return render(request, 'post.html', {'post': post})

def post_new_view(request):
    form = forms.CreatePost()
    return render(request, 'post_new.html', {'form': form})
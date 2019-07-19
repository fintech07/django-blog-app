from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name='home.html'
    context_object_name='all_posts_list'

class PostDetailView(DetailView):
    model = Post
    template_name='post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


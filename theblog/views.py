from turtle import st
from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Category, Post
from theblog.forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'


    ordering = ['-date']
    
class PostView(DetailView):
    model = Post
    template_name = 'theblog/post.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/createPost.html'

class CreateCategoryView(CreateView):
    model = Category
    template_name = 'theblog/createCategory.html'
    fields ='__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/updatePost.html'

class DeletePostView(DeleteView):
    model= Post
    template_name = 'theblog/deletePost.html'
    success_url = reverse_lazy('home')

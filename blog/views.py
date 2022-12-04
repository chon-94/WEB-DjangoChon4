from django.shortcuts import render
from django.views.generic import View,ListView, DetailView
from .models import Post, Script
from .forms import PostForm

class blogView(View):
    def get(self,request, *args, **kwargs):
        context={
            
        }
        return render(request,'blog/blog.html', context)

class ScriptsListView(ListView):
    model = Script

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
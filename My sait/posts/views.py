from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.

""" def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts":posts,
    }
    return render(request,"posts/list.html",context) """

class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"
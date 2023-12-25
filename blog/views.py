# from django.shortcuts import render
from .models import post

# from django.http import Http404
from django.views.generic import ListView, DetailView


class postListView(ListView):
    queryset = post.objects.all().order_by("-date")
    template_name = "blog/blog.html"
    context_object_name = "posts"
    paginate_by = 10


class postDetailView(DetailView):
    model = post
    template_name = "blog/post.html"

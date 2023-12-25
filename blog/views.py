from django.shortcuts import render
from .models import post


def list(request):
    data = {"posts": post.objects.all().order_by("-date")}
    return render(request, "blog/blog.html", data)

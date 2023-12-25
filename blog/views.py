from django.shortcuts import render
from .models import post
from django.http import Http404


def list(request):
    data = {"posts": post.objects.all().order_by("-date")}
    return render(request, "blog/blog.html", data)


def postContent(request, id):
    try:
        postContent = post.objects.get(id=id)
    except post.DoesNotExist:
        raise Http404("Bai viet khong ton tai")
    return render(request, "blog/post.html", {"post": postContent})

from django.shortcuts import render, get_object_or_404
from blog.models import comment, post as Post
from blog.forms import commentForm
from django.http import HttpResponseRedirect

# from django.http import Http404
from django.views.generic import ListView, DetailView


class postListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = "blog/blog.html"
    context_object_name = "posts"
    paginate_by = 10


# class postDetailView(DetailView):
#     model = post
#     template_name = "blog/post.html"


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = commentForm()
    if request.method == "POST":
        form = commentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post": post, "form": form})

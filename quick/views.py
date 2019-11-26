from django.shortcuts import render
from quick.models import Post


def post(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post
    }
    return render(request, "post.html", context)

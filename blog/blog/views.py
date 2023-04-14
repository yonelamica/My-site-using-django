from django.shortcuts import render, get_object_or_404
from .models import Post
def blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog.html', {'post': post})
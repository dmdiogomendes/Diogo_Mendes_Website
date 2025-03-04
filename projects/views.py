from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'index/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    return render(request, 'projects/post_detail.html', {'post': post})


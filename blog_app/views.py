from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request, pk):
    # Retrieve the specific post by its primary key (pk)
    # or return a 404 error if it doesn't exist
    posts = get_object_or_404(Post, pk=pk)

    context = {
        'posts': posts,
    }

    return render(request, 'blog_app/post_list.html', context)

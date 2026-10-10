from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from blog.forms import PostForm
from blog.models import Post

def post_list_view(request):
    post_list = Post.objects.filter(status=Post.Status.PUBLISHED)
    return render(request, 'blog/post_list.html', {'post_list':post_list})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post":post})

def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.method)
        if form.is_valid():
            form.save()
    form = PostForm()

    return render(request, "blog/post_create.html", {"form":form})

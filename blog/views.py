
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
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
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = get_user_model().objects.first()
            post.status = Post.Status.PUBLISHED
            post.save()
            return redirect("blog:post_list")
    form = PostForm()

    return render(request, "blog/post_create.html", {"form":form})

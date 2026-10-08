from django.shortcuts import render

from blog.models import Post

def post_list_view(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list':post_list})

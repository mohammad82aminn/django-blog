
from typing import Any

from django.shortcuts import render, redirect

from django.views import generic
from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment
from blog.models import Post

# def post_list_view(request):
#     post_list = Post.objects.filter(status=Post.Status.PUBLISHED).order_by("-datetime_created")
#     return render(request, 'blog/post_list.html', {'post_list':post_list})

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list_view"
    context_object_name = "post_list"
    queryset = (
        Post.objects.filter(status = Post.Status.PUBLISHED).order_by("-datetime_created")
    )


# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid:
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect("blog:post_detail", pk = post.pk)
#     else:
#         form = CommentForm()
        
#     comments = post.comments.all()
#     return render(request, "blog/post_detail.html", {"post":post, "comments":comments, "comment_form":form})

class PostDetailView(generic.DeleteView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        return context




# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.status = Post.Status.PUBLISHED
#             post.save()
#             return redirect("blog:post_list")
#     form = PostForm()

#     return render(request, "blog/post_create.html", {"form":form})

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_url = "/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = Post.Status.PUBLISHED
        return super().form_valid(form)

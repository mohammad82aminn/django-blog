from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path('create/', views.post_create_view, name="post_create"),
    path("<int:pk>/", views.PostDetailView.as_view(), name='post_detail'),
]
from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list_view, name="post_list"),
    path('create/', views.post_create_view, name="post_create"),
    path("<int:pk>/", views.post_detail_view, name='post_detail'),
]
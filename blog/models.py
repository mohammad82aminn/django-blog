
from django.conf import settings
from django.db import models


class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = "PUB", "Published"
        DRAFT = "DRF", "Draft"

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=3,
        choices=Status,
        default=Status.DRAFT,
    )
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


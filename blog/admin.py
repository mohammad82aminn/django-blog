from django.contrib import admin

from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "datetime_modified")
    list_filter = ("status", "datetime_created")
    search_fields = ("title", "text")
    ordering = ("-datetime_modified",)

    
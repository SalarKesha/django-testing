from django.contrib import admin
from django.contrib.admin import register
from post.models import Post

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'title', 'content')

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=1000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

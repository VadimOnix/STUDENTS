from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    like_count = models.IntegerField(default=0)

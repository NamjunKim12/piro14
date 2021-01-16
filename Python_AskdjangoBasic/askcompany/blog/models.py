from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignJey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author_name = models.CharField(max_length=100)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    
    
    
    
# Create your models here.

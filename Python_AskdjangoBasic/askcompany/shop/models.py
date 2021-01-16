from django.db import models
from django.conf import settings

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    is_publish = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.

class Post(models.Model):
    author = models.ForeignJey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)
    
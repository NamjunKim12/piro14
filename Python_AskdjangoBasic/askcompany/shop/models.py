from django.db import models
from django.conf import settings
from askcompany.utils import uuid_upload_to

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    is_publish = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
# Create your models here.f

    
    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)
    
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shop_post_set')

    
from django.db import models

# Create your models here.
class Post(models.Model):
    """
    class for a blog post
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  #sets on create
    updated = models.DateTimeField(auto_now=True)  #Updates on save


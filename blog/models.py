from django.contrib import admin
from django.conf import settings  # Imports Django's loaded settings
from django.db import models


# Create your models here.
class Post(models.Model):
    """
    class for a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        null=True,
        unique_for_date='published',
    )
    content = models.TextField()
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )
    created = models.DateTimeField(auto_now_add=True)  #sets on create
    updated = models.DateTimeField(auto_now=True)  #Updates on save

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Django auth user model
        on_delete=models.PROTECT,  # prevents deletion
        related_name='blog_posts', # the name that appears on the user model
        null=True
    )


    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible'
    )

    class Meta:
        ordering = ['-created']

        #sort by created in descending order

    def __str__(self):
        return self.title



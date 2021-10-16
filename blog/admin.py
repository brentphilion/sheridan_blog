from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',
    )
    list_filter = (
        'status',
    )
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.
admin.site.register(models.Post, PostAdmin)


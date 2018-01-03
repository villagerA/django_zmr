from django.contrib import admin
from .models import Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'post', 'created_time', 'email']

admin.site.register(Comment, PostAdmin)

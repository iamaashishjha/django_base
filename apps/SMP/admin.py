from django.contrib import admin
from .models import Post,  Comment, Tag, Like, Follow # Import your models

# Register your models with the admin site
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
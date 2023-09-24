from django.db import models
from django.utils import timezone
from config.base.model import BaseModel  # Import the BaseModel
from django.contrib.auth.models import CustomUser


class Post(BaseModel):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    description = models.CharField(max_length=30,null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    class Meta:
        get_latest_by = ['-created_at', '-updated_at']

    def __str__(self):
        return self.title[0:50]


class Comment(BaseModel):    
    content = models.TextField(null=True, blank=True)
    posts = models.ForeignKey(CustomUser, null=True, blank=True,on_delete=models.CASCADE, related_name='posts_comments', db_column='posts_id')

class Tag(BaseModel):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)

class Like(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, null=True, blank=True,on_delete=models.CASCADE, related_name='user_likes', db_column='user_id')
    posts = models.ForeignKey(CustomUser, null=True, blank=True,on_delete=models.CASCADE, related_name='posts_likes', db_column='posts_id')

class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, null=True, blank=True,on_delete=models.CASCADE, related_name='follower_follows', db_column='follower_id')
    following = models.ForeignKey(CustomUser, null=True, blank=True,on_delete=models.CASCADE, related_name='following_follows', db_column='following_id')


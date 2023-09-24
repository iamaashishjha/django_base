from django.db import models
from django.utils import timezone
from Authentication.models import CustomUser

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='created_%(class)ss', db_column='created_by')
    deleted_by = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='deleted_%(class)ss', db_column='deleted_by')
    updated_by = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='updated_%(class)ss', db_column='updated_by')

    class Meta:
        abstract = True  # Make this an abstract base model

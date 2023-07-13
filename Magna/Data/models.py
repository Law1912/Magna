from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Research(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    data = models.JSONField(blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    label = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['level']

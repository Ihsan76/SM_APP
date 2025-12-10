# mahwar_social/models.py
from django.contrib.auth.models import User
from django.db import models

class Album(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mahwar_albums'
    )
    name = models.CharField(max_length=100)
    size_mb = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'مسودة'),
        ('scheduled', 'مجدول'),
        ('published', 'منشور'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mahwar_posts'
    )
    content = models.TextField()
    platforms = models.JSONField(default=dict)  # {"instagram": true, "x": true}
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    scheduled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"

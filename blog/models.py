"""Blog related models."""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

USERS = User.objects.all()
USER_CHOICES = ((u.get_full_name(), u.get_full_name()) for u in USERS)


class Blog(models.Model):
    """Model for blog content."""

    slug = models.SlugField()
    title = models.CharField(max_length=300, default='')
    subtitle = models.CharField(max_length=300, default='')
    publish_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    author = models.CharField(max_length=300, choices=USER_CHOICES, default='')
    lede = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')

    class Meta:
        """Set name for admin screen."""

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

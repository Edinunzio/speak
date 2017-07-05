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


def map_blogs_to_author(query):
    """Method that returns object of mapped blogs to user."""

    author_data = []
    for a in query:
        fullname = a.get_full_name()
        blogs = Blog.objects.filter(author__iexact=fullname)
        _blogs = [
            {
                'title': blog.title,
                'slug': blog.slug,
                'lede': blog.lede
            } for blog in blogs
        ]

        author_data.append({'author': fullname, 'blogs': _blogs})
    return author_data

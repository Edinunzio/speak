"""Blog related models."""
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    """Author extension of User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Blog(models.Model):
    """Model for blog content."""

    slug = models.SlugField()
    title = models.CharField(max_length=300, default='')
    subtitle = models.CharField(max_length=300, default='')
    publish_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author)
    lede = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')

    class Meta:
        """Set name for admin screen."""

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.author.save()

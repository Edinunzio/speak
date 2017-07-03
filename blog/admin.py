# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    """Set up admin fields for Blogs."""

    list_display = (
        'title',
        'is_published',
        'publish_date',
        'author',
        'slug',
    )
    list_filter = (
        'publish_date',
        'is_published',
        'author',
        'title',
        'publish_date',
    )
    ordering = ['-publish_date']

admin.site.register(Blog, BlogAdmin)

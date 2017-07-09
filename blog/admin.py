# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Author, Blog, Image, Style


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


class AuthorAdmin(admin.ModelAdmin):
    """Set up admin fields for authors."""

    list_display = (
        'full_name',
    )

    def full_name(self, obj):
        first_name = obj.user.first_name
        last_name = obj.user.last_name
        return first_name + ' ' + last_name


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Image)
admin.site.register(Style)

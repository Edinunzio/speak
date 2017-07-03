# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Blog
from django.contrib.auth.models import User


def get_user_name(username):
    """Temp helper method to return full name."""
    user = User.objects.get(username=username)
    fullname = user.first_name + ' ' + user.last_name
    return fullname


def index(request):
    """Landing page for all blogs."""
    results = {}
    blogs = Blog.objects.filter(is_published=True).order_by('-publish_date')
    results['blogs'] = blogs

    return render(request, 'index.html', results)


def detail(request, slug):
    """Renders individual blog post."""
    results = {}
    blog = Blog.objects.get(slug__iexact=slug)
    results['author'] = get_user_name(blog.author)
    results['blog'] = blog

    return render(request, 'detail.html', results)

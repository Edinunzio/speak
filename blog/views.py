# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Blog


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
    results['blog'] = blog

    return render(request, 'detail.html', results)

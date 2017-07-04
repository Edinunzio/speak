# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Blog
from django.contrib.auth.models import User


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


def about(request):
    """About page."""

    return render(request, 'about.html', None)


def authors(request):
    """About page."""
    _authors = User.objects.filter(is_staff=True)
    results = {}
    author_data = []
    for a in _authors:
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

    results['authors'] = _authors
    results['author_data'] = author_data

    return render(request, 'authors.html', results)

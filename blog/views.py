"""View methods."""
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Blog, map_blogs_to_author


class BlogListView(ListView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog_list.html'

    def get(self, request):
        """Landing page for all blogs."""
        results = {}
        results['blogs'] = []
        for blog in self.queryset:
            results['blogs'].append(blog)
        return render(request, 'blog_list.html', results)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'


class AboutDetailView(ListView):
    model = Blog
    template_name = 'about.html'

    def get(self, request):
        """About page."""

        return render(request, 'about.html', None)


def authors(request):
    """About authors page."""
    _authors = User.objects.filter(is_staff=True)
    results = {}
    author_data = map_blogs_to_author(_authors)

    results['author_data'] = author_data

    return render(request, 'authors.html', results)

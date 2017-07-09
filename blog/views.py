"""View methods."""
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Author, Blog


class BlogListView(ListView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog_list.html'

    def get(self, request):
        """Landing page for all blogs."""
        queryset = self.queryset.filter(is_published=True)
        results = {}
        results['blogs'] = []
        for blog in queryset:
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


class AuthorListView(ListView):
    model = Author

    def get(self, request):
        """Author List page."""
        queryset = Author.objects.all()
        blogs = Blog.objects.all()
        results = {}
        results['authors'] = []
        for a in queryset:
            results['authors'].append(
                {'name': a.__str__(), 'blogs': blogs.filter(author=a.id)}
            )

        return render(request, 'author_list.html', results)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

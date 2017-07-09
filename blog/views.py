"""View methods."""
from __future__ import unicode_literals

from django.contrib.auth.models import User
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
    template_name = 'blog_detail.html'


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
                {
                    'name': a.__str__(),
                    'blogs': blogs.filter(author=a.id),
                    'username': a.user.username
                }
            )

        return render(request, 'author_list.html', results)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

    def get(self, request, username):
        _user = User.objects.get(username=username)
        results = {}
        author = Author.objects.get(user=_user.id)
        results['author'] = author
        """Author detail page."""

        return render(request, 'author_detail.html', results)

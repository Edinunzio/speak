"""ecms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from blog import views

from django.conf.urls import url
from django.contrib import admin

from .settings import URL_ADMIN

urlpatterns = [
    url(URL_ADMIN + '/', admin.site.urls),
    url(
        regex=r'^$',
        view=views.BlogListView.as_view(),
        name='get'
    ),
    url(
        regex=r'^blog/(?P<slug>[-\w]+)/$',
        view=views.BlogDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^authors/$',
        view=views.AuthorListView.as_view(),
        name='authors'
    ),
    url(
        regex=r'^author/(?P<username>[-\w]+)/$',
        view=views.AuthorDetailView.as_view(),
        name='author'
    ),
]

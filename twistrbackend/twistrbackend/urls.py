"""twistrbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users_views
from posts import views as posts_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/users/$', users_views.users_list),
    url(r'^api/users/(?P<pk>[0-9]+)$', users_views.users_detail),
    url(r'^api/posts/$', posts_views.posts_list),
    url(r'^api/posts/(?P<pk>[0-9]+)$', posts_views.posts_detail),
    url(r'^api/userline/(?P<pk>[0-9]+)$', posts_views.posts_by_user),
    # url(r'^api/usertags/(?P<pk>[0-9]+)$', posts_views.tags_by_user),
]

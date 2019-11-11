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
from django.conf.urls import include
from users import views as users_views
from posts import views as posts_views
from twists import views as twists_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^api/auth/', include('knox.urls')),
    url(r'^api/users/$', users_views.users_list),
    url(r'^api/users/delete/(?P<pk>[0-9]+)$', users_views.user_delete),
    url(r'^api/users/register/$', users_views.user_register, name='create-account-test'),
    url(r'^api/users/$', users_views.users_list),
    url(r'^api/users/(?P<pk>[0-9]+)$', users_views.users_detail),
    url(r'^api/users/login/$', users_views.user_login),

    url(r'^api/posts/$', posts_views.posts_list),
    url(r'^api/posts/(?P<pk>[0-9]+)$', posts_views.posts_detail),
    url(r'^api/userline/(?P<pk>[0-9]+)$', posts_views.posts_by_user),

    url(r'^api/tags/$', posts_views.tags_list),
    url(r'^api/tags/(?P<pk>[0-9]+)$', posts_views.tags_detail),
    url(r'^api/usertags/(?P<pk>[0-9]+)$', posts_views.tags_by_user),
    url(r'^api/posttags/(?P<pk>[0-9]+)$', posts_views.tags_by_post),

    url(r'^api/twists/$', twists_views.twists_list),
    url(r'^api/twists/(?P<pk>[0-9]+)$', twists_views.twists_detail),
    url(r'^api/unfollow/$', twists_views.unfollow),
    url(r'^api/userstwists/(?P<pk>[0-9]+)$', twists_views.twists_by_user),
    url(r'^api/userlinetwists/(?P<pku>[0-9]+)/(?P<pka>[0-9]+)$', twists_views.twists_by_author),
    # url(r'^api/twists/(?P<pk>[0-9]+)$', users_views.follower_count),
    # url(r'^api/twists/(?P<pk>[0-9]+)$', users_views.following_count),
    # Get followers by user
    # Get following by user
    url(r'^api/password/$', users_views.password_by_user),
]

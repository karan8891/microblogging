from django.conf.urls import url
from django.contrib import admin

from .views import (
    comment_thread,
    comment_delete

    )
# two urls for comment operations
urlpatterns = [
    url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
    url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]

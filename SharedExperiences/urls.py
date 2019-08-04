from django.conf.urls import url
from . import views
app_name='SharedExperiences'

urlpatterns=[
    url(r'^getBlogApi/(?P<id>[1-9][0-9]*)$', views.getBlogApi.as_view(), name='getBlogApi'),
    url(r'^getAllBlogs/(?P<id>[1-9][0-9]*)/'
    r'(?P<genre>[a-zA-Z]*)$',views.getAllBlogs.as_view(),name='getAllBlogs'),
    url(r'^getTopBlog/(?P<genre>[a-zA-Z]*)$',views.getTopBlog.as_view(),name='getTopBlog')
]
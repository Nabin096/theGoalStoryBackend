"""TheGoalStory URL Configuration

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
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from .adminViews import *
from SharedExperiences import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogsCreate', admin.site.admin_view(blogsCreate), name='blogsCreate'),
    url(r'^blogsTitleCreate', admin.site.admin_view(blogsTitleCreate), name='blogsTitleCreate'),
    url(r'^blogsSubmit', admin.site.admin_view(blogsSubmit), name='blogsSubmit'),
    url(r'^discardBlog', admin.site.admin_view(discardBlog), name='discardBlog'),
    url(r'^SharedExperiences/', include('SharedExperiences.urls')),

]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

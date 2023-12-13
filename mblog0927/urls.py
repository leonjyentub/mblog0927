"""
URL configuration for mblog0927 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mysite import views as mv
from mytest import views as testv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.homepage, name="homepage"),
    path('post/<slug:slug>/', mv.showpost, name="showpost"),
    path('post/', mv.show_all_posts, name="show-all-posts"),
    path('post/<int:post_id>/comments', mv.show_comments, name='show-comments'),
    path('about/', mv.about),
    path('about/<int:num>', mv.about, name='about'),
    path('carlist/', mv.carlist),
    path('carlist/<int:maker>/', mv.carlist, name='carlist-url'),
    path('post/new', mv.new_post, name="post-new"),
]

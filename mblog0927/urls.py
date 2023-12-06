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
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('post/<slug:slug>/', views.showpost, name="showpost"),
    path('post/', views.show_all_posts, name="show-all-posts"),
    path('post/<int:post_id>/comments', views.show_comments, name='show-comments'),
    path('about/', views.about),
    path('about/<int:num>', views.about, name='about'),
    path('carlist/', views.carlist),
    path('carlist/<int:maker>/', views.carlist, name='carlist-url'),
    path('post/new', views.new_post, name="post-new"),
]

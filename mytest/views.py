from django.shortcuts import render, redirect
from mytest.models import Post, Mood

# Create your views here.
def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    if request.method == 'GET':
        return render(request, 'myform.html', locals())
    elif request.method == 'POST':
        pass
    else:
        pass
from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    
def showpost(request, slug):
    post = Post.objects.get(slug=slug) 
    return render(request, 'post.html', locals())
    #select * from post where slug=%slug
    
import random
def about(request, num=-1):
    quotes = ['今日事，今日畢',
              '要怎麼收穫，先那麼栽',
              '知識就是力量',
              '一個人的個性就是他的命運']
    if num == -1 or num > 4:
        quote = random.choice(quotes)
    else:
        quote = quotes[num]
    return render(request, 'about.html', locals())   



'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter, post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
'''
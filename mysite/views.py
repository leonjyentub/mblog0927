from django.shortcuts import render
from mysite.models import Post, Comment
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    hour = now.timetuple().tm_hour
    years = range(1960,2024)
    return render(request, 'index.html', locals())
    
def show_all_posts(request):
    posts = Post.objects.all()
    return render(request, 'allposts.html', locals())

def showpost(request, slug):
    post = Post.objects.get(slug=slug) 
    return render(request, 'post.html', locals())
    #select * from post where slug=%slug
    
def show_comments(request, post_id):
    #comments = Comment.objects.filter(post=post_id)
    comments = Post.objects.get(id=post_id).comment_set.all()
    return render(request, 'comments.html', locals())
    
    
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

def carlist(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [
        [{'model':'Fiesta', 'price': 203500},
            {'model':'Focus','price': 605000}, 
            {'model':'Mustang','price': 900000}],
		[{'model':'Fit', 'price': 450000}, 
		 {'model':'City', 'price': 150000}, 
		 {'model':'NSX', 'price':1200000}],
		[{'model':'Mazda3', 'price': 329999}, 
		 {'model':'Mazda5', 'price': 603000},
		 {'model':'Mazda6', 'price':850000}],]

    maker = maker
    maker_name =  car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())

'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter, post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
'''

def new_post(request):
    print(f'form method: {request.method}')
    if request.method == 'GET':
        return render(request, 'myform_1.html', locals())
    elif request.method == 'POST':
        title = request.POST['title']
        slug = request.POST['slug']
        content = request.POST['content']
        category = request.POST.getlist('category')
        post = Post(title=title, slug=slug, body=content, category=category)
        post.save()
        return render(request, 'myform_1.html', locals())
    '''
    try:
        username = request.GET['user_id']
        password = request.GET['password']
        print(f'username:{username}, password:{password}')
        return render(request, 'myform_1.html', locals())
    except:
        return render(request, 'myform_1.html', locals())
    '''
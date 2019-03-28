from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post, User

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .forms import JoinForm, PostForm

from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)

from django.core.paginator import Paginator

from urllib.request import urlopen
from bs4 import BeautifulSoup


def home(request):
    return render(request, 'post/iz_one.html')


def post(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,9)    #페이지 네이션
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts':posts}
    return render(request, 'post/post.html', context)

def join(request): 
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('join')
    else:
        form = JoinForm()
        args = {'form': form}
        return render(request, 'post/join.html', args)

@login_required(login_url="/login")
def write(request):   #게시글 쓰기
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False) #commit = False 뜻은 DB에 바로 저장 안한다. 
            instance.user =  request.user
            instance.save()
        return redirect('post')
    else:
        form= PostForm()
        return render(request,'post/write.html',{'form':form})


@login_required(login_url="/login")
def delete(request,pk):   #게시글 삭제
    post =  Post.objects.get(pk=pk)
    if post.user == User.objects.get(username = request.user.get_username()):
        post.delete()
        return redirect('post')
    else:
        return redirect('/')


@login_required(login_url="/login")
def index(request,pk):  #게시글 번호및 내용
    posts = Post.objects.filter(pk=pk)
    context = {'posts':posts}
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    post.post_hit +=1 #조회수
    post.save()
    return render(request, 'post/index.html',context)


@login_required(login_url="/login")
def edit(request,pk):
    post = get_object_or_404(Post , pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance =post)
        if form.is_valid():
            if post.user == User.objects.get(username = request.user.get_username()):
                form.save()
            else:
                return redirect('/')
        return redirect('post')
    else:
        form = PostForm(instance = post)
    context = {
        'form':form,
        'post':post,
    }
    return render(request,'post/edit.html',context)

#def crawl(request):

    #html = urlopen("http://iz-one.co.kr/photos/")  

    #bsObject = BeautifulSoup(html, "html.parser") 

    #a = bsObject.find("div",{"class":"site-main"})

    #b = a.find_all('a')
    #return HttpResponse(b)


login = LoginView.as_view(template_name='post/login.html')

logout = LogoutView.as_view()
# Create your views here.

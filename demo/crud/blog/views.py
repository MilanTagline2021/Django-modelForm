from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import SigUpForm, LoginForm, PostForm
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{"posts":posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request,'blog/dashboard.html',{"posts":posts})
    else:
        return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method == 'POST':
        form=SigUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations you are become Author.")
            form.save()
    form=SigUpForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if not   request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully !!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=LoginForm()
            return render(request,'blog/login.html',{'form':form})
    return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                post=Post(title=title,desc=desc)
                post.save()
                form=PostForm()
        form=PostForm()
        return render(request, 'blog/add-post.html',{'form':form})
    else:
        return HttpResponseRedirect('/login')

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            ps=Post.objects.get(pk=id)
            form=PostForm(request.POST, instance=ps)
            if form.is_valid():
                form.save()
        else:
            ps=Post.objects.get(pk=id)
            form=PostForm(instance=ps   )
        return render(request, 'blog/update-post.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pk=Post.objects.get(pk=id)
            pk.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
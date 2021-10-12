from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from first_app.models import User
from .forms import StudentRegistration

# Create your views here.

# add new item show value into table
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = make_password(fm.cleaned_data['password'])
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration(request.POST)  
    fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'first_app/addandshow.html',{'form':fm,'stu':stud})

# update data function
def update_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'first_app/updatestudent.html',{'form':fm})


# delete data 
def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
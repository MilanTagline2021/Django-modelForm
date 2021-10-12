from django import forms
from django.shortcuts import render
from .models import Student, Manage, RestInform
from .forms import StudentRegistration, PostRegistration, TeacherRegistration, ManageDetail
# Create your views here.

def student_info(request):
    stud=Student.objects.all()
    return render(request,'enroll/studetails.html', {'stu':stud})

def showformdata(request):
    fm = StudentRegistration()
    return render(request,'enroll/stuforms.html',{'form':fm})

def showstudentdata(request):
    if request.method == 'POST':
        pr=PostRegistration(request.POST)
        if pr.is_valid():
            print('Name : ',pr.cleaned_data['name'])
            print('Email : ',pr.cleaned_data['email'])
            print('Contact : ',pr.cleaned_data['contact_detail'])           
    else:
        pr=PostRegistration()
        print('from get request')

    return render(request, 'enroll/postforms.html',{'form':pr})

def showteacherdata(request):
    if request.method == 'POST':
        tr=TeacherRegistration(request.POST)
        if tr.is_valid():
            nm = tr.cleaned_data['name']
            em = tr.cleaned_data['email']
            ps = tr.cleaned_data['password']
            cp = tr.cleaned_data['confirm_password']
            if ps != cp:
                raise forms.ValidationError('Password does not match')
            tm = Manage(name=nm, email=em, password=ps, confirm_password=cp)
            tm.save()    

    tr = TeacherRegistration()
    return render(request, 'enroll/teacher.html',{'form':tr})

def showmanagedetail(request):
    if request.method == 'POST':
        tr=ManageDetail(request.POST)
        print(tr['name'])
        if tr.is_valid():
            nm = tr.cleaned_data['name']
            em = tr.cleaned_data['email']
            ps = tr.cleaned_data['password']
            cp = tr.cleaned_data['confirm_password']
            if ps != cp:
                raise forms.ValidationError('Password does not match')
            tm = RestInform(name=nm, email=em, password=ps, confirm_password=cp)
            tm.save()    

    tr = ManageDetail()
    return render(request, 'enroll/manage.html',{'form':tr})
        
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from first_app.models import User
from django.views.generic import TemplateView, RedirectView
from django.views import View
from .forms import StudentRegistration

# Create your views here.

# add new item show value into table
class UserAddShowView(TemplateView):
    template_name='first_app/addandshow.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stud':stud, 'form':fm}
        return context

    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')


# update data function
class UserUpdateView(View):
    def get(self, request, id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        return render(request,'first_app/updatestudent.html',{'form':fm})
 
    def post(self, request, id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')

# delete data
class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['id']
        User.objects.get(pk=delete_id).delete()
        return super().get_redirect_url(*args, **kwargs)

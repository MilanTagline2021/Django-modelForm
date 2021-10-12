from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def learn_django(request):
    course_name={'name':'Django'}
    return render(request, 'home.html',course_name)


def learn_python(request):
    return HttpResponse("<h1>Hello Python!!!</h1>")

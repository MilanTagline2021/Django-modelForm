from django.urls import path
from . import views

urlpatterns = [
    path('stu/', views.student_info),
    path('form/',views.showformdata),
    path('note/',views.showstudentdata),
    path('teacher/',views.showteacherdata),
    path('manage/',views.showmanagedetail),
]
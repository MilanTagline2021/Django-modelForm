from django.urls.conf import path

from first_app import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout ,name='logout'),
    path('add/', views.add_post ,name='add-post'),
    path('update/<int:id>', views.update_post ,name='update-post'),
    path('delete/<int:id>', views.update_post ,name='delete-post'),
]


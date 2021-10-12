from django.contrib import admin
from enroll.models import Student, Manage, RestInform
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stui','stuname','stuemail','stupass')

@admin.register(Manage)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

@admin.register(RestInform)
class RestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')

# admin.site.register(Student, StudentAdmin)

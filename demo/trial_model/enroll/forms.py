from django import forms
from django.forms import widgets
from .models import RestInform

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

class PostRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    contact_detail = forms.IntegerField()
    
class TeacherRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class ManageDetail(forms.ModelForm):
    class Meta:
        model = RestInform
        fields = ['name','email','password','confirm_password']
        widgets = {
            'password':forms.PasswordInput,
            'confirm_password':forms.PasswordInput,
            'name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Your Email'})
            } 
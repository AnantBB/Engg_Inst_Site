from django import forms
from .models import person_info
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User   

class person_info_form(ModelForm):
    class Meta:
        model = person_info        
        fields = ['academic_year', 'course','division', 'group' ,'arcadian', 'fname', 'mname', 
        'lname', 'mother_name', 'inst_code', 'mobile', 'whatsapp', 'email']
        QUALIFIER = (('1','Dr.'), ('2','Mr.'), ('3','Mrs.'), ('4','Miss'))
        widgets = {
            'arcadian': forms.Select(choices=QUALIFIER,attrs={'class': 'form-control' , 'style': 
            'width: 190px'}),
        }

class auth_user(UserCreationForm):
    class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
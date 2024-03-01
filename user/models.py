from django.db import models

from django import forms
from django.contrib.auth.models import User


# Create your models here.

class LogForm(forms.Form):
    usernema=forms.CharField(max_length=30)
    password=forms.CharField(max_length=40)



class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='amit')
    first_name=models.CharField(max_length=70)
    Last_name=models.CharField(max_length=70)
    dob=models.DateField(max_length=70)
    email=models.EmailField(max_length=70)
    address=models.TextField()

    class Meta:
        db_table='profile'



class Pr_Form(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'   



    

   
    
    

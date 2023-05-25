from django.contrib.auth.forms import UserCreationForm
from Shop.models import *
from django.forms import ModelForm
from django import forms


class CustomUserForm(UserCreationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter User Name"}))
  email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email Address"}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter the password"}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"RE-enter the password"}))
  
  
  class Meta:
    model   =User
    fields  =["username","email","password1","password2"]
    
    
    
class Create_cat(ModelForm):
  
   class Meta:
         model = Catagory
         fields = ["name", "image", "description", "status"]
         widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control','required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
         
class Create_Products(ModelForm):
  class Meta:
         model = Products
         fields = ["catagory","image", "name", "vendor", "quantity","original_price","Selling_price","description","status","trending"]
         widgets = {
            'catagory': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control','required': 'required'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'vendor': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'original_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'Selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trending': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
         
class Usertype(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =["usertype"]
        widgets = {
            'usertype': forms.Select(attrs={'class': 'form-control mb-3','required': 'required'}),
        }
        # usertype_value = Usertypeform.cleaned_data['usertype']
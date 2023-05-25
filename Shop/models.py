from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime
import os
# Create your models here.

def getfileName(request,filename):
  now_time =datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  
  return os.path.join("uploads/",new_filename)

class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image =models.ImageField(upload_to=getfileName,null=True,blank=True)
  description =models.TextField(max_length=500,null=False,blank=False)
  status =models.BooleanField(default=False,help_text="0-Show,1-Hidden")
  created_at = models.DateTimeField(auto_now_add=True)  
 


  def __str__(self):
    return self.name
  

class Products(models.Model):
  catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  image =models.ImageField(upload_to=getfileName,null=True,blank=True)
  vendor=models.CharField(max_length=150,null=False,blank=False)
  quantity = models.IntegerField(null=False,blank=False)
  original_price =models.FloatField(null=False,blank=False)
  Selling_price =models.FloatField(null=False,blank=False) 
  description =models.TextField(max_length=500,null=False,blank=False)
  status =models.BooleanField(default=False,help_text="0-Show,1-Hidden")
  trending = models.BooleanField(default=False,help_text="0 - non-trending,1-trending")
  created_at = models.DateTimeField(auto_now_add=True)  



  def __str__(self):
    return self.name
  
  
class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product = models.ForeignKey(Products,on_delete=models.CASCADE)
  product_qty = models.IntegerField(null=False,blank=False)
  created_at= models.DateTimeField(auto_now_add=True) 
  
  
  @property
  def total_cost(self):
    return self.product_qty*self.product.Selling_price
  

class Fav(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product = models.ForeignKey(Products,on_delete=models.CASCADE)
  created_at= models.DateTimeField(auto_now_add=True) 
  
class UserProfile(models.Model):
    USER_CHOICES = [
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100, choices=USER_CHOICES, blank=False)
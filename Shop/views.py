from django.http import JsonResponse
from django.shortcuts import render,redirect
from Shop.models import *
from django.contrib import messages
from Shop.form import *
from django.contrib.auth import authenticate,login,logout
import json

def home(request):
  products  = Products.objects.filter( trending=1)
  
  cat_name =Catagory.objects.all()
  
  # find user type  
  usertype =" "
  if request.user:
    user = request.user
    print(user)
    cat = UserProfile.objects.all()
    for i in cat:
      if i.user == user:
        
       usertype = str(i.usertype)
  
  
  return render(request,"index.html",context={"trend":products})

def index_trend(request,id):
  product = Products.objects.get(name=id)  
  category = product.catagory
  category_name = category.name
 

  return redirect('/ProductsDetail/'+category_name+"/"+id)

def login_page(request):
  if request.user.is_authenticated:
    return redirect('/')
  
  else:
    if request.method == "POST":
      name= request.POST.get('username')
      pwd= request.POST.get('Password')
      user = authenticate(request,username = name ,password = pwd )
      
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in SuccessFully")
        return redirect('/')      
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect('/login')

    
  return  render(request,"login.html")

def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged Out SuccessFully")
  return redirect('/')

def add_to_cart(request):
  print("===============")
  if request.headers.get('x-requested-with')=="XMLHttpRequest":
    if request.user.is_authenticated:
      print("===============3")
      
      data=json.load(request)
      product_Qty=data['p_qty']
      product_id=data['p_id']
      print(request.user.id)
      product_status = Products.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id,product_id=product_id):
           return JsonResponse({'status':'product Already in  Add cart'},status=200)
        else:
          if product_status.quantity >= product_Qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_Qty)
            return JsonResponse({'status':'successfully in   Add cart'},status=200)
          else:
            return JsonResponse({'status':'product Stock  not Available'},status=200)
      

    else:
      print("===============3") 
      return JsonResponse({'status':'Login to Add cart'},status=200)
  else:
    print("===============2")
    
    return JsonResponse({'status':'invaild Access'},status=200)

def add_to_fav(request):
  print("===============")
  if request.headers.get('x-requested-with')=="XMLHttpRequest":
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['p_id']
      print(request.user.id)
      product_status = Products.objects.get(id=product_id)
      if product_status:
        fav_status = Fav.objects.filter(user=request.user,product_id=product_id)
        if fav_status:
          return JsonResponse({'status':'Already in Favourtie'},status=200)
        else:
          Fav.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Successfully added'},status=200)
    
      else:
        return JsonResponse({'status':'Login to Add Favorite'},status=200)
    else:
      return JsonResponse({'status':'Login to Add Favorite'},status=200)
     
  else:
      return JsonResponse({'status':'invaild Access'},status=200)
      
  

def cart(request):
  if request.user.is_authenticated:
    cart =Cart.objects.filter(user=request.user)
    
    print(cart)
    return render(request,"shop/cart.html",{"cart":cart})
  else:
    return redirect('login')
  
def fav_page(request):
  if request.user.is_authenticated:
    fav =Fav.objects.filter(user=request.user)
    return render(request,"shop/fav.html",{"fav":fav})
  else:
    return redirect('login')

def remove_cart(request,id):
  
  remove_cart = Cart.objects.get(id=id)
  remove_cart.delete()

  return redirect('/cart')

def remove_fav(request,id):
  
  remove_cart = Fav.objects.get(id=id)
  remove_cart.delete()

  return redirect('/fav_page')

def Reg(request):
  usertype = Usertype()
  form=CustomUserForm()
  if request.method == 'POST':
    form = CustomUserForm(request.POST)
    Usertypeform = Usertype(request.POST)
    if form.is_valid():
      user=form.save()
      
      # usertype_value = Usertypeform.cleaned_data['usertype']
      
      # name_value = form.cleaned_data['username']
      usertype_value = request.POST.get('usertype')
      # print(Usertypeform)
      
      # user_profile = UserProfile(user=name_value,usertype=usertype_value)
      # user_profile.save()
      
      user_profile = UserProfile(user=user, usertype=usertype_value)
      user_profile.save()
      
      return redirect('/login')
  return render(request,"register.html",context={"form":form ,"user":usertype})

def collections(request):
  
  catagory  = Catagory.objects.filter(status=0)
  
  return render(request,"collection.html",context={"catagory":catagory})

def collectionsview(request,name):
  
  if(Catagory.objects.filter(name=name,status=0)):
     products= Products.objects.filter(catagory__name=name)  
     return render(request,"shop/products/products_index.html",context={"products": products,"name":name})

  else:
    messages.warning(request,"no such catagory Found")
    return
  
def ProductsDetail(request,c_name,p_name):
  if(Catagory.objects.filter(name=c_name,status=0)):
    if(Products.objects.filter(name=p_name,status=0)):
      products=Products.objects.filter(name=p_name,status=0).first()
      return render(request,"shop/products/products_details.html",context={"products":products,"c_name":c_name})
    else:
      messages.error(request,"nosuch Catagory Found")
      return redirect('collection')
  else:
    messages.error(request,"nosuch Catagory Found")
    return redirect('collection')
  
  
  
def create_Catagory(request):
  
  cat =Create_cat()
  if request.user.is_authenticated:
    if request.method == "POST":
      form = Create_cat(request.POST,request.FILES)
      if form.is_valid():
        form.save()
        messages.success(request,"Catorgray Succesfully created")
        return redirect('/upload_products')
      
    
    return render(request,"create/catatory.html",context={"cat":cat})
  return redirect('/login')
  
  

def create_Products(request):
  pro =Create_Products()
  if request.user.is_authenticated:
    if request.method == "POST":
      form = Create_Products(request.POST,request.FILES)
      if form.is_valid():
        form.save()
        messages.success(request,"Registration Success you can login NOW")
        return redirect('/')
      
    
    return render(request,"create/product.html",context={"pro":pro})
  return redirect('/login')
  
  
def seller(request):
  # find user type  
  usertype =" "
  if request.user:
    user = request.user
    print(user)
    cat = UserProfile.objects.all()
    for i in cat:
      if i.user == user:        
       usertype = str(i.usertype)
       
    return render(request,"create/seller.html",context={"Type":usertype})  
  
  return redirect("/login")

  
  
  
  
 
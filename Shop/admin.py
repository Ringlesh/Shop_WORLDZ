from django.contrib import admin
from Shop.models import *
# Register your models here.
class CatagoryAdmin(admin.ModelAdmin):
  list_display = ('name','image','description')

class ProductsAdmin(admin.ModelAdmin):
  list_display = ('name','image','description')

class CartAdmin(admin.ModelAdmin):
  list_display = ('user','product','product_qty')
  
class FavAdmin(admin.ModelAdmin):
  list_display = ('user','product')
  
class UserprofileAdmin(admin.ModelAdmin):
  pass
  
  
  
admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Fav,FavAdmin)
admin.site.register(UserProfile)

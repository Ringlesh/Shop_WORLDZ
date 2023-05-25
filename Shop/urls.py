from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [   
     path('',views.home,name='home'), 
     path('index_trend/<str:id>',views.index_trend,name='index_trend'),
     path('collection/',views.collections,name='collection'),
     path('Reg/',views.Reg,name='reg'),
     path('login/',views.login_page,name='login'),
     path('logout/',views.logout_page,name='logout'),
     path('collections/<str:name>',views.collectionsview,name='collectionveiw'),
     path('ProductsDetail/<str:c_name>/<str:p_name>',views.ProductsDetail,name='ProductsDetail'),
     path('addtocart/',views.add_to_cart,name='addtocart'),
     path('cart/',views.cart,name='cart'),
     path('removecart/<str:id>',views.remove_cart,name='remove_cart'),
     path('removefav/<str:id>',views.remove_fav,name='remove_fav'),
     path('fav/',views.add_to_fav,name='fav'),
     path('fav_page',views.fav_page,name='fav_page'),
     path('create_catagary',views.create_Catagory,name='ccat'),
     path('upload_products',views.create_Products,name='cpro'),
     path('seller',views.seller,name='seller'),  
    
]

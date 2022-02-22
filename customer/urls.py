from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
 
   path('contact',views.contact, name='contact'),
   path('about',views.about, name='about'),
   path('login',views.login, name='login'),
   path('register', views.register, name='register'),
   path('contact',views.contact, name='contact'),
   path('logout', views.logout, name='logout'),

   path('product',views.product, name='product'),

   path('cart', views.cart, name='cart'),
   path('add-to-cart/<int:product_id>/', views.add_cart, name="add-to-cart"),
   path('remove_item/<int:cart_item_id>/', views.remove_cart_item, name="remove_item"),

   path('purchaseitem/<int:product_id>/', views.purchaseitem, name="purchaseitem"),
   path('payment', views.payment, name='payment'),

   #admin
   path('admindashboard',views.admindashboard, name='admindashboard'),

   path('view-customer', views.view_customer, name='view-customer'),
   path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),

   path('admin-products', views.admin_products_view, name='admin-products'),
   path('delete-product/<int:pk>',views.delete_product_view, name='delete-product'),
   path('update-product/<int:pk>',views.update_product_view, name='update-product'),

   path('admin-view-booking', views.admin_view_booking_view, name='admin-view-booking'),
   path('delete-order/<int:pk>', views.delete_order_view, name='delete-order'),
   
]

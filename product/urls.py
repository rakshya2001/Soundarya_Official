
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from product import views

urlpatterns = [
    path('admin-products', views.admin_products_view,name='admin-products'),
    path('addproducts', views.add_products_view,name='addproducts'),
]
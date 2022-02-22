from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .forms import ProductForm


# Create your views here.

@login_required(login_url='admin')
def admin_products_view(request):
    products=models.Product.objects.all()

    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'products': paged_product,
    }
    return render(request,'adminControl/admin_product.html',data)

@login_required(login_url='admin')
def add_products_view(request):
    products = models.Product.objects.all()
    productForm = ProductForm()
    if request.method == 'POST':
        productForm = ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
        return HttpResponseRedirect('admin-products')
    return render(request, 'admincontrol/addproduct.html', {'productForm': productForm, 'products': products})
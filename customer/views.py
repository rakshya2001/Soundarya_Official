from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.core.mail import send_mail
from django.contrib.auth import  authenticate , get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from product import models
from product.forms import ProductForm

from  product.models import Cart, CartItem, Product, Orders
# Create your views here.
def home(request):
    products = models.Product.objects.all()
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'products': paged_product,
    }

    return render(request, 'Pages/homepage.html', data)

def contact(request):
    return render(request, 'Pages/Contact.html')

def about(request):
    return render(request, 'Pages/About.html')

def admindashboard(request):
    User = get_user_model()
    usercount=User.objects.all().order_by('username').filter(is_superuser=False).count()
    productcount=models.Product.objects.all().count()
    ordercount = Orders.objects.all().count()
    data = {
        'usercount':usercount,
        'productcount':productcount,
        'ordercount':ordercount,
    }

    return render(request, 'adminControl/admindashboard.html', data)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user.is_superuser:
            auth.login(request, user)
            return redirect('admindashboard')
        elif user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'pages/login.html')  


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        auth.login(request, user)
        user.save()
        return redirect('login')
    else:
        return render(request, 'pages/registration.html')    


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email'] 
        message =request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            # settings.EMAIL_HOST_USER,
            #           ['riyastha406@mail.com'],
            ['bhattarakshya6@gmail.com' ], #To email
            # fail_silently= True,
        )   
        return render(request, 'pages/Contact.html', {'message_name': message_name}) 

    else:
        return render(request, 'pages/Contact.html' , {})     


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are successfully logged out.')
        return redirect('login')
    return redirect('home')

def product(request):
    products = models.Product.objects.all()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'products': paged_product,
    }

    return render(request, 'Pages/Products.html', data)

def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id


def cart(request, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.all().filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart, is_active=True)
    except:
        # print("except")
        pass

    context = {
        "cart_items": cart_items,
    }

    return render(request, 'Pages/cart.html', context)

def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)

    if request.method == "POST":

        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
        if is_cart_item_exists:
            return redirect('cart')
        else:
            cart_item = CartItem.objects.create(
                product=product,
                cart=cart,
                user=current_user,
            )
            cart_item.save()

        return redirect('cart')

def remove_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def payment(request):
    return render(request,'Pages/payment.html')


def purchaseitem(request, product_id):
    if request.method == "POST":
        current_user = request.user
        product = Product.objects.get(id=product_id)
        
        order = Orders(user=current_user, product=product)
        order.save()

        cart_item_id  = request.POST['cart_item_id']
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        return redirect('payment')



# @login_required(login_url='adminlogin')
def view_customer(request):
    User = get_user_model()
    users=User.objects.all().order_by('username').filter(is_superuser=False)
    paginator = Paginator(users, 1)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'users': paged_product,
    }

    return render(request,'admincontrol/view_customer.html',data)

# @login_required(login_url='admin')
def delete_customer_view(request,pk):
    users=User.objects.get(id=pk)
    users.delete()
    return redirect('view-customer')  

def admin_products_view(request):
    products = models.Product.objects.all()
    products=models.Product.objects.order_by('-name')
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'products': paged_product,
    }
    return render(request, 'admincontrol/admin_product.html', data)   

def delete_product_view(request, pk):
    products = models.Product.objects.get(id=pk)
    products.delete()
    return redirect('admin-products')

def update_product_view(request, pk):
    products = models.Product.objects.get(id=pk)
    productForm = ProductForm(instance=products)
    if request.method == 'POST':
        productForm = ProductForm(
            request.POST, request.FILES, instance=products)
        if productForm.is_valid():
            productForm.save()
            return redirect('admin-products')
    return render(request, 'adminControl/update_product.html', {'productForm': productForm, 'products': products})


def admin_view_booking_view(request):
    order = Orders.objects.all()
    paginator = Paginator(order, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'order': paged_product,
    }
    return render(request, 'admincontrol/view_booking.html', data)

def delete_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')
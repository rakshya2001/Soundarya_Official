from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from django.test import TestCase
from customer.views import home, about, login, register, contact, logout, product, cart, payment, admindashboard

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_home_url(self):
        url=reverse("home")
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)

    def test_case_about_url(self):
        url=reverse("about")
        print(resolve(url))
        self.assertEquals(resolve(url).func,about)
    
    def test_case_login_url(self):
        url=reverse("login")
        print(resolve(url))
        self.assertEquals(resolve(url).func,login)
    
    def test_case_register_url(self):
        url=reverse("register")
        print(resolve(url))
        self.assertEquals(resolve(url).func,register)
    
    def test_case_contact_url(self):
        url=reverse("contact")
        print(resolve(url))
        self.assertEquals(resolve(url).func,contact)
    
    def test_case_logout_url(self):
        url=reverse("logout")
        print(resolve(url))
        self.assertEquals(resolve(url).func,logout)
    
    def test_case_product_url(self):
        url=reverse("product")
        print(resolve(url))
        self.assertEquals(resolve(url).func,product)
    
    def test_case_cart_url(self):
        url=reverse("cart")
        print(resolve(url))
        self.assertEquals(resolve(url).func,cart)
    
    def test_case_payment_url(self):
        url=reverse("payment")
        print(resolve(url))
        self.assertEquals(resolve(url).func,payment)
    
    def test_case_admindashboard_url(self):
        url=reverse("admindashboard")
        print(resolve(url))
        self.assertEquals(resolve(url).func,admindashboard)
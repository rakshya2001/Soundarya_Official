from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Pages/homepage.html')

def contact(request):
    return render(request, 'Pages/Contact.html')

def about(request):
    return render(request, 'Pages/About.html')
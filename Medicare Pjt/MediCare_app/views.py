from django.shortcuts import render

# Create your views here.

def homepage(request):

    return render(request,'home_page.html')


def register(request):

    return render(request,'user_reg_page.html')

def login(request):
    return render(request,'login_page.html')



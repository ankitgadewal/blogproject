from django.shortcuts import render
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, render, redirect
# from blogs.models import Blogs
# Create your views here.
def users(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        print(email, phone, password)
        new = Users(email=email, password=password, phone=phone)
        new.save()
    return render(request, 'users.html')

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confpassword = request.POST['confpassword']
        phone = request.POST["phone"]

        #some checks
        if len(username)<10 or len(password)<8 or len(phone)<10:
            return HttpResponse("Please fill the form correctly")
        elif password!=confpassword:
            return HttpResponse("passwords did not match please refill the form")
        else:
            newuser = User.objects.create_user(username, email, password)
            newuser.save()
            return HttpResponse("Sign up successful")

def userlogin(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        loginuser = authenticate(username=loginusername, password=loginpassword)

        if loginuser:
            login(request, loginuser)
            return render(request, 'userlogin.html', {'loginuser': loginuser})
        else:
            return HttpResponse("bad credentials")

def userlogout(request):
    logout(request)
    return redirect(to='/users')

def newblog(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        slug = request.POST['slug']

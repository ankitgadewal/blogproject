from django.shortcuts import render
from .models import NewBlog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, render, redirect
from blogs.models import Blogs
from django.contrib import messages

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
            messages.error(request, "please fill the form correctly")
            return redirect(to='/users')
        elif password !=confpassword:
            messages.error(request, "password didn't match")
            return redirect(to='/users')

        else:
            messages.success(request, "you are now registered")
            newuser = User.objects.create_user(username, email, password)
            newuser.save()
            return redirect(to='/users')

def userlogin(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        loginuser = authenticate(username=loginusername, password=loginpassword)

        if loginuser:
            login(request, loginuser)
            return render(request, 'userlogin.html', {'loginuser': loginuser})
        else:
            messages.error(request, "Bad Credentials... Try again!!")
            return redirect(to='/users')

def userlogout(request):
    logout(request)
    messages.success(request, "you are logged out successfully")
    return redirect(to='/users')

def newblog(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        slug = request.POST['slug']

        Blogs(title=title, description=description, slug=slug).save()
        messages.success(request, "your post has been posted successfully!!! you can now see it on blog page")
        return render(request, 'postadded.html')



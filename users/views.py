from django.shortcuts import render
from .models import Users
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


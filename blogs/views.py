from django.shortcuts import render
from .models import Blogs

# Create your views here.
def index(request):
    allposts = Blogs.objects.all()
    return render(request, 'index.html', {'allposts': allposts})

def users(request):
    return render(request, 'users.html')
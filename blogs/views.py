from django.shortcuts import render
from .models import Blogs

# Create your views here.
def blog(request):
    allposts = Blogs.objects.all()
    return render(request, 'blog.html', {'allposts': allposts})

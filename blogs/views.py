from django.shortcuts import render
from .models import Blogs
from django.contrib import messages

# Create your views here.
def blog(request):
    allposts = Blogs.objects.all()
    onepost = Blogs.objects.filter().first()
    return render(request, 'blog.html', {'allposts': allposts, 'onepost': onepost})

def index(request):
    allposts = Blogs.objects.all()
    return render(request, 'index.html', {'allposts': allposts})

def search(request):
    query = request.GET['query']
    if len(query) > 50 or len(query)<1:
        allposts = []
    else:
        allposts = Blogs.objects.filter(title__icontains=query).union(Blogs.objects.filter(description__icontains=query))
    return render(request, 'search.html', {'allposts': allposts, 'query': query})

def blogpost(request, slug):
    allposts = Blogs.objects.filter(slug=slug)
    print(allposts)
    return render(request, 'blogpost.html', {'allposts':allposts})

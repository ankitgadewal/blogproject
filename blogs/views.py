from django.shortcuts import render
from .models import Blogs

# Create your views here.
def blog(request):
    allposts = Blogs.objects.all()
    return render(request, 'blog.html', {'allposts': allposts})

def index(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allposts = []
    else:
        allposts = Blogs.objects.filter(title__icontains=query).union(Blogs.objects.filter(description__icontains=query))
    return render(request, 'search.html', {'allposts': allposts, 'query': query})

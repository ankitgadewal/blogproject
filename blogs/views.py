from django.shortcuts import render
from .models import Blogs

# Create your views here.
def blog(request):
    allposts = Blogs.objects.all()
    print(allposts)
    # onepost = Blogs.objects.filter(title__icontains='django')
    onepost = Blogs.objects.get(id=8)
    print(onepost)
    return render(request, 'blog.html', {'allposts': allposts, 'onepost': onepost})

def index(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allposts = []
    else:
        allposts = Blogs.objects.filter(title__icontains=query).union(Blogs.objects.filter(description__icontains=query))
    return render(request, 'search.html', {'allposts': allposts, 'query': query})

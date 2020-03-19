from django.shortcuts import render, redirect, HttpResponse
from .models import Blogs, Comment
from django.contrib import messages
from users.views import userlogin

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
    allcomments = Comment.objects.all()
    return render(request, 'blogpost.html', {'allposts':allposts, 'allcomments':allcomments})

def comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        Comment(comment=comment).save()
        return HttpResponse("Comment added")
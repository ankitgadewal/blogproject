from django.shortcuts import render, HttpResponse
from blogs.models import Comment
def comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        Comment(comment=comment).save()

    return render(request, 'postadded.html')
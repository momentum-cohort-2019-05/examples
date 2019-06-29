from django.shortcuts import render

from .models import Comment

# Create your views here.
def index(request):
    """render the homepage with all comments"""
    comments = Comment.objects.filter()
    
    context = {
        'comments': comments
    }
    return render(request, 'index.html', context=context)
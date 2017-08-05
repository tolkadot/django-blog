from django.shortcuts import render
from django.utils import timezone
#from django.contrib.auth.models import User
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.filter(author=User.objects.get(username='tolkadot'))
    return render(request, 'blog/post_list.html', {'blog' : posts})

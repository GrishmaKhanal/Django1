from django.shortcuts import render
from blog.models import Blog
# Create your views here.
def blogview(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blog' : blogs})

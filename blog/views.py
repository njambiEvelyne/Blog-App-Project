from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Dummy data to be accessed by thetemplate

def home_message (request):
  context = {
    'posts': Posts.objects.all()
  }
  return render(request, 'blog/home.html', context)

def hello(request):
  return HttpResponse('<h3>Welcome to the website</h3>')

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})


from django.shortcuts import render
from django.http import HttpResponse

# Dummy data to be accessed by thetemplate
posts = [

  {
    'author': 'CoreyMS',
    'title' :'Blog-post 1',
    'content':'First post content',
    'darte_posted': 'August 27, 2018'
  },
  {
    'author': 'Jane Doe',
    'title' :'Blog-post 2',
    'content':'Second post content',
    'darte_posted': 'August 28, 2018'
  }
]

def home_message (request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def hello(request):
  return HttpResponse('<h3>Welcome to the website</h3>')

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})


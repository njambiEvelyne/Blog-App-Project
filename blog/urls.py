from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_message, name= 'blog-home'),
    path("hello/", views.hello, name='hello-page'),
    path ("about/", views.about, name= 'blog-about'), 
    
]


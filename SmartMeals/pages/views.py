from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(response, *args, **kwargs):
    # return HttpResponse("<h1>TEST</h1>")
    return render(response, 'home.html', {})

def about_view(response, *args, **kwargs):
    return render(response, 'about.html', {})
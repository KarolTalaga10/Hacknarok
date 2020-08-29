from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(response, *args, **kwargs):
    return render(response, 'home.html', {})
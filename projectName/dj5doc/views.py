from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'dj5doc/home.html')

def start(request):
    return render(request, 'dj5doc/start.html')

def tutorial02(request):
    return render(request, 'dj5doc/tutorial02.html')

# def home(request):
#     return HttpResponse('This is home test')

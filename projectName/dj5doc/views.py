from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'dj5doc/home.html')

def start(request):
    return render(request, 'dj5doc/start.html')

def tutorial02(request):
    return render(request, 'dj5doc/tutorial02.html')

def codepractice(request):
    name = "MD. ABDUL KADER"
    country = "Bangladesh"
    skills = ["Python", "Django", "HTML"]
    data = {"name": name, "country": country, "skills": skills}
    return render(request, 'dj5doc/codepractice.html', data)

def marketplace(request):
    return render(request, 'dj5doc/marketplace.html')

def about(request):
    return render(request, 'dj5doc/about.html')

def contacts(request):
    return render(request, 'dj5doc/contacts.html')

# def home(request):
#     return HttpResponse('This is home test')

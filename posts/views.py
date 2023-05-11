from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect

from datetime import date

current_date = date.today()
print(current_date)




# Create your views here.

def now_date(request):
    if request.method == "GET":
        return HttpResponse(current_date)

def hello_view(request):
    if request.method == "GET":
        return HttpResponse('Hello! Its my project!')


def redirect_to_google(request):
    if request.method == "GET":
        return redirect('https://www.google.com/')


def redirect_to_youtube(request):
    if request.method == "GET":
        return redirect('https://www.youtube.com/')


def redirect_to_git(request):
    if request.method == "GET":
        return redirect('https://www.github.com/')

def goodbye(request):
    if request.method == "GET":
        return HttpResponse("Goodby user!")


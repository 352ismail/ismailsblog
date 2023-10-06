from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request , "base_layout.html")


def home(request):
    return render(request , "index.html")
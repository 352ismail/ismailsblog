from django.shortcuts import render
from . models import Articles
from django.http import HttpResponse


# Create your views here.

def index(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/index.html' , {'articles':articles})


def article_detail(request, slug):
    article_details = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'artcile_details': article_details})
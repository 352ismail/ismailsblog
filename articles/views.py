from django.shortcuts import render , redirect
from . models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms


# Create your views here.

def index(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/index.html' , {'articles':articles})

@login_required(login_url="/account/login")
def article_create(request):
    if request.method == 'POST':
        form = forms.Create_Article(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/articles/create')      
    else:
        form = forms.Create_Article()
    return render(request, 'articles/create.html',{'form':form})


def article_detail(request, slug):
    article_details = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'artcile_details': article_details})
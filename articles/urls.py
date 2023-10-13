from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.article_create, name="create_article"),
    path('<slug:slug>', views.article_detail, name="article_details"),
]
from django.shortcuts import render
from . import Article

def article_list(request):
    articles= Article.objects.all().order_by('date') 
    return render(request, 'articles/article_list.html',{'articles':articles})
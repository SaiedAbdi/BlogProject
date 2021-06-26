from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def all_articles(request):
    all_articles = Article.objects.filter(status = 'publish')
    context = {'all_articles':all_articles}

    return render (request,'blog/all_articles.html', context)

def article_detail(request, id, slug):
    # article =  Article.objects.get(id = id, slug = slug)
    article = get_object_or_404(Article,id=id,slug=slug)
    return render(request,'blog/article.html',{'article':article})
 
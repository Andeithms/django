from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Relationship, Tag


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all().order_by(ordering)
    related = Relationship.objects.all()
    context = {'object_list': articles, 'related': related}

    return render(request, template, context)

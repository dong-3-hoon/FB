from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer

# Create your views here.
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    # get이면 하나만 가져와서 many = true 노필요
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['GET'])
def article_search_title(request, article_title):
        articles = Article.objects.filter(title__contains=article_title)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/detail.html', context)


# 하나의 create함수에서 2 가지 요청을 처리 가능함
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content=request.POST.get('content')
    
        # db에 새로운 Article 저장
        # Article.objects.create(
        #     title=title,
        #     content=content
        # )
        article=Article(title=title, content=content)
        article.save()
        # 어디에다가 요청을 보
        return redirect('articles:index')
    else:
        return render(request, 'articles/create.html')
    # foward 방식(render): 요청, 응답 정보를 그대로 계속 가져감(페이지만 바뀜, url 유지)
    # system의 변화가 생기지 않는 단순 조회 요청
    # redirect 방식: 새로운 요청을 생성(기존 요청, 응답 정보가 제거,ur 변경)
    # 시스템에 변화가 생기는 새로운 요청

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article=Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
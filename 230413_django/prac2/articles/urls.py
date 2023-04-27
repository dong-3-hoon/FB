from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<article_title>/', views.article_search_title),
]

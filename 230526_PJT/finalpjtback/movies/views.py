
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators - 함수를 꾸며주는 함수
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer
from .models import Movie, Comment, Genre
from django.contrib.auth import get_user_model



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_list(request):
    if request.method == 'GET':
        # movies = Movie.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'POST'])
def recommend_movies(request, weather):
    if weather == "now":
        movie = Movie.objects.order_by('-release_date')[:40]
    elif(weather=='Rainy'):
        genre = Genre.objects.filter(name__in=['액션', '코미디']).distinct()
        genre_ids = []
        for i in genre:
            genre_ids.append(i.id) 
        movie=Movie.objects.filter(genre_ids__in=genre_ids, vote_average__gt=8).distinct().order_by('-vote_average')
    elif(weather=='Snow'):
        genre = Genre.objects.filter(name__in=['드라마', '로맨스'])
        genre_ids = []
        for i in genre:
            genre_ids.append(i.id) 
        movie=Movie.objects.filter(genre_ids__in=genre_ids, vote_average__gt=8).distinct().order_by('-vote_average')
    elif(weather=='Clear'):
        genre = Genre.objects.filter(name__in=['공포', '범죄', '스릴러'])
        genre_ids = []
        for i in genre:
            genre_ids.append(i.id) 
        movie=Movie.objects.filter(genre_ids__in=genre_ids, vote_average__gt=8).distinct().order_by('-vote_average')
    else :
         movie=Movie.objects.filter(vote_average__gt=8).order_by('-vote_average')
    serializer = MovieListSerializer(movie, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request, movie_pk):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        movie = Movie.objects.get(pk=movie_pk)
        comments = Comment.objects.filter(movie=movie)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    user = get_object_or_404(get_user_model(), username=request.user)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

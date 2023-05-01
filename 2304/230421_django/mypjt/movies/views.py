from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Actor, Review
from .serializers import ActorListSerializer, ActorSerializer
from .serializers import MovieListSerializer, MovieSerializer
from .serializers import ReviewListSerializer, ReviewSerializer

@api_view(["GET", "POST"])
def actor_list(request):
    if request.method == "GET":
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ActorListSerializer(data=request.data)
        # raise_exception : 유효하지 않은 데이터로 요청할 때
        # 서버 잘못이 아닌 클라이언트 잘못!
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "DELETE", "POST"])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    
    if request.method == "GET":
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    elif request.method == "DELETE":
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MovieListSerializer(data=request.data)
        # raise_exception : 유효하지 않은 데이터로 요청할 때
        # 서버 잘못이 아닌 클라이언트 잘못!
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(["GET", "DELETE", "PUT"])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(["GET", "POST"])
def review_list(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ReviewListSerializer(data=request.data)
        # raise_exception : 유효하지 않은 데이터로 요청할 때
        # 서버 잘못이 아닌 클라이언트 잘못!
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(["GET", "DELETE", "PUT"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(["GET", "POST"])
def movie_reviews(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == "GET":
        comments = movie.comment_set.all()
        serializer = ReviewSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
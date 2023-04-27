from rest_framework import serializers
from .models import Movie, Actor, Review

class Ref_MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =('title',)
class Ref_ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields =('title', 'content',)
class Ref_ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields =('name',)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields =('title', 'content')
        
class ReviewSerializer(serializers.ModelSerializer):
    movie = Ref_MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields ='__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =('title', 'overview')

class MovieSerializer(serializers.ModelSerializer):
    actors = Ref_ActorSerializer(many=True, read_only=True)
    review_set = Ref_ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields ="__all__"

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields ='__all__'

class ActorSerializer(serializers.ModelSerializer):
    movie_set = Ref_MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = "__all__"
from rest_framework import serializers
from .models import Movie, Comment, Genre
from accounts.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('name',)

class MovieListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)
    genre_ids = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'overview', 'poster_path', 'genre_ids', 'release_date')
        read_only_fields=('genre_ids',)
        


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user')


class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user', )




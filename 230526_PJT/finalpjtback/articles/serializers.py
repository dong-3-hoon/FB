from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = '__all__'
        read_only_fields = ('user',)



class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user')


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'username',)


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('profile_image',)
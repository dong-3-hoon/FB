from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    # comment_Set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['comment'] = rep.pop('comment_set', [])
        return rep
    
    class Meta:
        model = Article
        fields = "__all__"
        
class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ("id", "title", "content")
        
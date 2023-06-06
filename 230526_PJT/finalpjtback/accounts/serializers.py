from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import PasswordChangeSerializer
import base64

class FollowersSerializer(serializers.ModelSerializer):
    class Meta :
        model = get_user_model()
        fields = ('nickname',)

class UserSerializer(serializers.ModelSerializer):
    followers = FollowersSerializer(many=True)
   
    class Meta:
        model = get_user_model()
        
        # fields = ("id", "username", "first_name", "last_name", "email", "followings")
        fields = "__all__"
        read_only_fields = ('followers',)
class ProfileSerializer(serializers.ModelSerializer):
    followers = FollowersSerializer(many=True)   
    class Meta:
        model = get_user_model()
        
        # fields = ("id", "username", "first_name", "last_name", "email", "followings")
        fields = "__all__"
        read_only_fields = ('followers',)
        




    
        
class CustomPasswordChangeSerializer(PasswordChangeSerializer):
    pass
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
#         extra_kwargs = {'password': {'write_only': True}}  # 비밀번호 필드 설정

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = self.Meta.model(**validated_data)
#         user.set_password(password)  # 비밀번호 설정
#         user.save()
#         return user
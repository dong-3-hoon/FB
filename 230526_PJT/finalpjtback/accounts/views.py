from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from .forms import UserForm
from django.conf import settings
from django.http import FileResponse

import base64


# 유저 정보 확인
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userinfo(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)



# @api_view(['POST'])
# def signup(request):
#   serializer = UserSerializer(data=request.data)
#   if serializer.is_valid():
#       serializer.save()  # 사용자 데이터 저장
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 회원 정보 수정
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def update(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    if request.method == 'POST':
        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            # 이미지 업데이트를 위한 추가 로직
            profile_image = request.FILES.get('profile_image')  # 업로드된 이미지 가져오기
            if profile_image:
                user.profile_image = profile_image  # 이미지 필드에 할당
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

# 닉네임 업데이트
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_nickname(request):
    user = get_user_model().objects.get(username=request.user)
    nickname = request.data.get('nickname')
    user.nickname = nickname
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data)

# # 프로필 사진 수정
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def update_profile(request, user_pk):
#     user = get_user_model().objects.get(pk=user_pk)
#     profile = request.POST.get('profile')
#     pass



# 팔로우
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserSerializer(request.user)
    if request.method == 'POST' : 
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
            # if request.user in person.followers.all():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
    return Response(serializer.data)
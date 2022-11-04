from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from users.models import User
from users.serializers import UserModifySerializer, UserSerializer, UserBookmarkSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

# 마이 페이지(유저 프로필, 북마크)
class MyPageView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user) # ProfileSerializer에서 북마크(역참조), 유저 프로필 정보(닉네임, 프사, 관심장르, 소개글) 가져와야함
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserModifySerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
<<<<<<< Updated upstream
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
=======
            return Response(serializer.data, status=status.HTTP_200_OK)


>>>>>>> Stashed changes
class BookmarkView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserBookmarkSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

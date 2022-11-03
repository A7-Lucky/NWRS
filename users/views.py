from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer, ProfileSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



class SignupView(APIView):
    def get(self, request):  # 추후 프론트 연결 시 고려사항
        if not request.user.is_authenticated:
            return Response({"message": "로그인이 필요합니다"}, 401)
        else:
            return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


# 프론트 연결 시 SignupView 와 마찬가지로 get 에 대한 고려 필요
# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


# 마이 페이지
class MyPageView(APIView):
    def get(self, request):
        pass

    def delete(self, request):
        pass


# 프로필 수정 페이지
class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = ProfileSerializer(user)

        return Response(serializer.data)

    def put(self, request):
        pass
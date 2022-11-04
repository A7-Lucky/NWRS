from dataclasses import field
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User
from webtoon.serializers import WebtoonSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class UserModifySerializer(serializers.ModelSerializer):
    bookmark_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ("favorite", "introduce", "profile_img", "bookmark_set",)


class UserBookmarkSerializer(serializers.ModelSerializer):
    bookmark_set = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ("bookmark_set",)



class TokenObtainPairSerializer:
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
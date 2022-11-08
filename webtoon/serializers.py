from rest_framework import serializers
from webtoon.models import Genre, Webtoon, Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    webtoon = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_webtoon(self, obj):
        return obj.webtoon.title

    class Meta:
        model = Review
        fields = "__all__"

class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = ("user", "comment", "my_score", "webtoon")

# 장르 표기를 id 대신 name 으로 변경
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)

class WebtoonSerializer(serializers.ModelSerializer):
    # Reviews = ReviewSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Webtoon
        fields = "__all__"
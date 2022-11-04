from rest_framework import serializers
from webtoon.models import Webtoon, Review


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
    class Meta:
        model = Review
        fields = ("user", "comment", "my_score", "webtoon")

class WebtoonSerializer(serializers.ModelSerializer):
    # Reviews = ReviewSerializer(many=True)

    class Meta:
        model = Webtoon
        fields = "__all__"
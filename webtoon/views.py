from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from webtoon.models import Webtoon, Review
from users.models import User
from webtoon.serializers import WebtoonSerializer, ReviewSerializer, ReviewCreateSerializer
from webtoon.collaborative_filtering import item_based_filtering

# 웹툰 리스트
class WebtoonView(APIView):
    def get(self, request):
        # 전체 웹툰 무작위 정렬 보여주기
        webtoons = Webtoon.objects.order_by('?')[:10]
        serializer = WebtoonSerializer(webtoons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):  # 테스트용 코드
        serializer = WebtoonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 웹툰 상세 페이지
class WebtoonDetailView(APIView):
    def get(self, request, webtoon_id): 
        # article = Article.objects.get(id=article_id)
        webtoon = get_object_or_404(Webtoon, id=webtoon_id)
        serializer = WebtoonSerializer(webtoon)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 웹툰 상세 페이지의 전체 리뷰 리스트 및 작성
class WebtoonReviewView(APIView):
    def get(self, request, webtoon_id):
        webtoon = get_object_or_404(Webtoon, id=webtoon_id)
        reviews = webtoon.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, webtoon_id):
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, webtoon_id=webtoon_id)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 사용자 검증
class WebtoonReviewDetailView(APIView):
    def put(self, request, webtoon_id, review_id):
        review = get_object_or_404(Review, id=review_id)
        if request.user == review.user:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, webtoon_id, review_id):
        review = get_object_or_404(Review, id=review_id)
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)


# 내가 작성한 리뷰 전체
class MyReviewView(APIView):
    def get(self, request):
        user = request.user
        reviews = user.reviews_user.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 리뷰 수정/삭제
class MyReviewDetailView(APIView):
    def put(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if request.user == review.user:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)


class BookmarkView(APIView):
    def post(self, request, webtoon_id):
        webtoon = get_object_or_404(Webtoon, id=webtoon_id)
        if request.user in webtoon.bookmark.all():
            webtoon.bookmark.remove(request.user)
            return Response("북마크를 취소했습니다.", status=status.HTTP_200_OK)
        else:
            webtoon.bookmark.add(request.user)
            return Response("북마크 했습니다.", status=status.HTTP_200_OK)


class RecommendView(APIView):
    def get(self, request, webtoon_id):
        webtoons = []
        a = get_object_or_404(Webtoon, id=webtoon_id)
        b = item_based_filtering(a.title)
        for i in b:
            c = get_object_or_404(Webtoon, title=i)
            webtoons.append(c)
        # print(webtoons)
        serializer = WebtoonSerializer(webtoons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WebtoonSearchView(ListAPIView):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonSerializer
    filter_backends = [SearchFilter]
    search_fields = ('title',)

from django.urls import path
from webtoon import views


urlpatterns = [
    path('', views.WebtoonView.as_view(), name='webtoon_view'),
    path('<int:webtoon_id>/', views.WebtoonDetailView.as_view(), name='Webtoon_detail_view'),
    path('<int:webtoon_id>/review/', views.ReviewView.as_view(), name='review_view'),
    path('<int:webtoon_id>/review/<int:review_id>', views.ReviewDetailView.as_view(), name='reviewdetail_view'),
    path('<int:webtoon_id>/bookmark/', views.BookmarkView.as_view(), name='bookmark_view'),
]
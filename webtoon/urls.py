from django.urls import path
from webtoon import views


urlpatterns = [
    path('', views.WebtoonView.as_view(), name='webtoon_view'),
    path('<int:webtoon_id>/', views.WebtoonDetailView.as_view(), name='Webtoon_detail_view'),
    path('<int:webtoon_id>/review/', views.WebtoonReviewView.as_view(), name='webtoon_review_view'),
    path('<int:webtoon_id>/review/<int:review_id>/', views.WebtoonReviewDetailView.as_view(), name='webtoon_review_detail_view'),
    path('myreview/', views.MyReviewView.as_view(), name='my_review_view'),
    path('myreview/<int:review_id>/', views.MyReviewDetailView.as_view(), name='my_review_detail_view'),
    path('<int:webtoon_id>/bookmark/', views.BookmarkView.as_view(), name='bookmark_view'),
    path('<int:webtoon_id>/practice/', views.PracticeView.as_view(), name='Webtoon_practice_view'),

]
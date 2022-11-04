from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sign-up/', views.SignupView.as_view(), name="signup_view"),
    path('mypage/<int:user_id>/', views.MyPageView.as_view(), name="mypage_view"),
    path('mypage/bookmark/<int:user_id>/', views.BookmarkView.as_view(), name="bookmark_view"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
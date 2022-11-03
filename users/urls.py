from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sign-up/', views.SignupView.as_view(), name="signup_view"),
    path('mypage/', views.MyPageView.as_view(), name="mypage_view"),
    path('profile/<int:user_id>/', views.ProfileView.as_view(), name="profile_view"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
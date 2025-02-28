from django.urls import path

from .views import CustomTokenVerifyView, CustomTokenRefreshView, CustomTokenObtainPairView, \
    LogoutView

urlpatterns = [
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # logins in user
    path('jwt/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('logout/', LogoutView.as_view(), name='token_logout'),
]

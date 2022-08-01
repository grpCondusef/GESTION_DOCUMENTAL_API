from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from USER_APP.api.views import registration_view, login_view, Logout, GetUserDataView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', registration_view  , name='register'),
    path('login/',login_view , name ='login'),
    path('logout/',Logout.as_view() , name ='logout'),
    path('data/',GetUserDataView.as_view(), name='datos-usuario'),
    path('user-edit/<int:id>', GetUserDataView.as_view(), name='user-edit'),

    path('api/token/',TokenObtainPairView.as_view() , name ='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view() , name ='token_refresh'),
]
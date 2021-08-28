from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
# Profiles PATHS
    path('api/profiles', views.ProfileList.as_view(), name='profile_list'),

    path('api/profiles/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),

# User PATHS and LOGIN
    path('api/users', views.UserAccountList.as_view(), name='user_detail'),

    path('api/users/<int:pk>', views.UserAccountDetail.as_view(), name='user_detail'),

    path('api/users/login', csrf_exempt(views.check_user_login), name='check_user_login')

]

from django.urls import path
from . import views

urlpatterns = [
# Profiles PATHS
    path('api/profiles', views.ProfileList.as_view(), name='profile_list'),
    path('api/profiles/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
]

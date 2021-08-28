# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProfileSerializer
from .serializers import UserAccountSerializer
from .models import Profile
from .models import UserAccount

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

# Product Views
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

# User Account Views
class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

# User Auth Function
def check_user_login(request):
    if request.method=='GET':
        return JsonResponse({})

    if request.method=='PUT':
        jsonRequest = json.loads(request.body)
        username = jsonRequest['username']
        password = jsonRequest['password']
        if UserAccount.objects.get(username=username):
            user = UserAccount.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'id':user.id, 'username':user.username})
            else:
                return JsonResponse({})
        else:
            return JsonResponse({})

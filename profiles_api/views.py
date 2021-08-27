# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProfileSerializer
from .models import Profile

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

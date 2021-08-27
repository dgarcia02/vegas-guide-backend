from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'image', 'dob', 'email', 'phone', 'city', 'state', 'interest', 'attended', 'wishlist',)
    

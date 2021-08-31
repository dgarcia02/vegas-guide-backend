from rest_framework import serializers
from .models import Profile
from .models import UserAccount
from django.contrib.auth.hashers import make_password, check_password

# serializers make the data into a json format
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'image', 'dob', 'email', 'phone', 'city', 'state', 'interest', 'attended', 'wishlist', 'first_name', 'gender', 'last_name',)

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'password', 'is_active',)

    def create(self, validated_data):
        user = UserAccount.objects.create(
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        user = UserAccount.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data['password'])
        user.save()
        return user

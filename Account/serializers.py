from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password', 'phone_number', 'role')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role']
        )
        # Create profile based on role
        if user.role == CustomUser.TRAINEE:
            TraineeProfile.objects.create(user=user)
        elif user.role == CustomUser.MEMBER:
            MemberProfile.objects.create(user=user)
        elif user.role == CustomUser.ADMIN:
            AdminProfile.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
    
    
class TraineeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraineeProfile
        fields = ['id', 'user', 'bio', 'certifications', 'specialization']

class MemberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberProfile
        fields = ['id', 'user', 'membership_date', 'membership_type']

class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = ['id', 'user', 'role']
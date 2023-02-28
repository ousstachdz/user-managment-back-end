from rest_framework import serializers

from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name',
            'last_login', 'date_joined', 'username',
            'email', 'profile'
        ]

        extra_kwargs = {
            'email': {'read_only': True},
            'username': {'read_only': True}
        }

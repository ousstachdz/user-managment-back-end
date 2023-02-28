from rest_framework import serializers

from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserBasicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name',
        ]


class UserDetailsSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password', 'user_permissions', 'groups', 'user_ptr']

        extra_kwargs = {
            'email': {'read_only': True},
            'username': {'read_only': True}
        }

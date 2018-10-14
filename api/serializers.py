from rest_framework import serializers
from service.models import Company, Family, Guide, User


class GuideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guide
        fields = (
            'id',
            'created_at',
            'updated_at',
            'first_name',
            'last_name',
            'phone_number',
            'email'
        )


class UserSerializer(serializers.ModelSerializer):
    activation_code = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            'id',
            'created_at',
            'updated_at',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'activation_code',
            'password',
            'family'
        )

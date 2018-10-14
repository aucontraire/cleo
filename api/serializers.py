from rest_framework import serializers
from service.models import Company, Family, Guide, User


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id',
            'created_at',
            'updated_at',
            'name',
            'address'
        )


class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = (
            'id',
            'created_at',
            'updated_at',
            'due_date',
            'birth_date',
            'baby_gender',
            'main_address',
            'company',
            'guide'
        )


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

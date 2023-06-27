from django.contrib.auth import (
    authenticate,
    password_validation,
)
from django.contrib.auth.hashers import make_password
from django.core import exceptions
from rest_framework import serializers

from employees.models import Employee


class EmployeeCreateSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password_repeat',
        )
        extra_kwargs = {
            'id': {'required': False},
            'password': {'write_only': True},
        }

    def create(self, validate_data):
        password = validate_data.get('password')
        password_repeat = validate_data.pop('password_repeat')

        try:
            password_validation.validate_password(password=password)
        except exceptions.ValidationError as error:
            error_dict = {'password': error.messages}
            raise serializers.ValidationError(detail=error_dict)

        if password_repeat != password:
            error_dict = {
                'password': ['the password and the repeat password must match.']
            }
            raise serializers.ValidationError(
                detail=error_dict
            )

        validate_data['password'] = make_password(password)

        return super().create(validate_data)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'is_active': {'read_only': True},
            }


class EmployeeLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Employee
        fields = (
            'username',
            'password',
        )

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        employee = authenticate(
            username=username,
            password=password
        )

        if not employee:
            raise exceptions.ValidationError('Incorrect username or password.')

        return employee


class EmployeeLogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id',)
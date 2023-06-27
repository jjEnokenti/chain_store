from django.contrib.auth import (
    login,
    logout,
)
from rest_framework import (
    generics,
    status,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from employees import serializers


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = serializers.EmployeeCreateSerializer


class EmployeeLoginSerializer(generics.GenericAPIView):
    serializer_class = serializers.EmployeeLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = serializer.save()
        login(request=request, user=employee)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeLogoutView(generics.GenericAPIView):
    serializer_class = serializers.EmployeeLogoutSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        logout(request)

        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    http_method_names = ('get', 'put', 'patch', 'delete',)

    def get_object(self):
        return self.request.user

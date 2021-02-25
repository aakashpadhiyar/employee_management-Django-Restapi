from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'age', 'city')


class UserSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, queryset=Employee.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'employees')
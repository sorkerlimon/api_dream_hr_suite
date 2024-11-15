from rest_framework import serializers
from .models import User, Role, LoginLog, BrowserHistory, ApplicationUsage, ScreenshotLog


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()  # Nested serialization for Role

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'name', 'role', 'created_at', 'is_active', 'is_staff']


class LoginLogSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = LoginLog
        fields = '__all__'


class BrowserHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = BrowserHistory
        fields = '__all__'


class ApplicationUsageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ApplicationUsage
        fields = '__all__'


class ScreenshotLogSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ScreenshotLog
        fields = '__all__'

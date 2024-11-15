from rest_framework import viewsets
from .models import User, Role, LoginLog, BrowserHistory, ApplicationUsage, ScreenshotLog
from .serializers import (
    UserSerializer,
    RoleSerializer,
    LoginLogSerializer,
    BrowserHistorySerializer,
    ApplicationUsageSerializer,
    ScreenshotLogSerializer,
)


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginLogViewSet(viewsets.ModelViewSet):
    queryset = LoginLog.objects.all()
    serializer_class = LoginLogSerializer


class BrowserHistoryViewSet(viewsets.ModelViewSet):
    queryset = BrowserHistory.objects.all()
    serializer_class = BrowserHistorySerializer


class ApplicationUsageViewSet(viewsets.ModelViewSet):
    queryset = ApplicationUsage.objects.all()
    serializer_class = ApplicationUsageSerializer


class ScreenshotLogViewSet(viewsets.ModelViewSet):
    queryset = ScreenshotLog.objects.all()
    serializer_class = ScreenshotLogSerializer

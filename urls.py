from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet,
    UserViewSet,
    LoginLogViewSet,
    BrowserHistoryViewSet,
    ApplicationUsageViewSet,
    ScreenshotLogViewSet,
)

router = DefaultRouter()
router.register('roles', RoleViewSet)
router.register('users', UserViewSet)
router.register('login-logs', LoginLogViewSet)
router.register('browser-histories', BrowserHistoryViewSet)
router.register('application-usages', ApplicationUsageViewSet)
router.register('screenshot-logs', ScreenshotLogViewSet)

urlpatterns = router.urls

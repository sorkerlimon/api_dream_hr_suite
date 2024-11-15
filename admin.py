from django.contrib import admin
from .models import User, Role, LoginLog, BrowserHistory, ApplicationUsage, ScreenshotLog

admin.site.register(User)
admin.site.register(Role)
admin.site.register(LoginLog)
admin.site.register(BrowserHistory)
admin.site.register(ApplicationUsage)
admin.site.register(ScreenshotLog)

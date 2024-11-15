from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings
import os,uuid

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number is required")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    # Required methods for custom user models
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Login Logs Model
class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True, blank=True)
    break_start = models.DateTimeField(null=True, blank=True)
    break_end = models.DateTimeField(null=True, blank=True)
    total_working_time = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"Log {self.id} for {self.user.phone_number}"

# Browser History Model
class BrowserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    browser_name = models.CharField(max_length=50)
    visited_url = models.TextField()
    visit_time = models.DateTimeField()

    def __str__(self):
        return f"Browser History {self.id} for {self.user.phone_number}"

# Application Usage Model
class ApplicationUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"App Usage {self.id} for {self.user.phone_number}"



def screenshot_upload_path(instance, filename):
    """
    Create a unique filename by appending a UUID.
    Path: screenshots/<user_phone_number>/<unique_filename>
    """
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4().hex}.{ext}"
    return f'screenshots/{instance.user.phone_number}/{unique_filename}'

class ScreenshotLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to=screenshot_upload_path)  # Dynamic upload path
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Screenshot {self.id} for {self.user.phone_number}"

    def delete(self, *args, **kwargs):
        """Delete the file when the object is deleted."""
        if self.image_path:
            if os.path.isfile(self.image_path.path):
                os.remove(self.image_path.path)
        super().delete(*args, **kwargs)
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='آدرس ایمیل',
        max_length=255,
        null=True,
        blank=True,
        unique=True,
    )
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر ', null=True, blank=True)
    phone_active_code = models.DateTimeField(null=True, blank=True, verbose_name=' فعال سازی شماره همراه')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    fullname = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=12, unique=True,
                             verbose_name="شماره همراه")
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_admin = models.BooleanField(default=False, verbose_name="ادمین")

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otp(models.Model):
    token = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone



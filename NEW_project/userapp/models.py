from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        if password is None:
            raise TypeError(
                'Superuser must have a password'
            )
        user = self.create_user(phone=phone, password=password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13, unique=True)
    USERNAME_FIELD = 'phone'
    objects = UserManager()

    def __str__(self):
        return 'User — ' + self.phone

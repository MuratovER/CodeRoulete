from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('Users must have an email adress')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self):
        pass

class Profile(AbstractBaseUser, PermissionsMixin):
    filter_choice = (
        ('No Filter', 'No Filter'),
        ('Filter by Language', 'Filter by Language'),
        ('Filter by Code', 'Filter by Code')
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    github = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    code_language = models.CharField(max_length=50)
    code_sphere = models.CharField(max_length=50)
    search_filter = models.CharField(max_length=18, choices=filter_choice)
    is_active = models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        return self.nickname

    def __str__(self):
        return self.nickname
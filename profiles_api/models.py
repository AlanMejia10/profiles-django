from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# this class tells django how to add users as we changed the user table
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    # functions specified in this class are used to manipulate objects within
    # the model that manager is for, the create_user and create_superuser will be
    # called by the manager cli when creating users
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("email must be provided")

        email = self.normalize_email(email)

        # creates a model that the manager is representing
        user = self.model(email=email, name=name)
        user.set_password(password)
        # its best practise to indicate the database we are going to use
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create superuser with give details"""
        user = self.create_user(email=email, name=name, password=password)
        # super user atribb is created by the permissions mixin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom Model Manager for users
    objects = UserProfileManager()

    # overrides the default username to be the email field, this one is required
    # by default
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    # string representacion of the model object
    def __str__(self):
        return self.email

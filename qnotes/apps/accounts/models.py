from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class SiteUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            username=username,
            email=SiteUserManager.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class SiteUser(AbstractBaseUser):
    username = models.CharField(_('Username'), max_length=40, unique=True, db_index=True)
    email = models.EmailField(_('Email'), max_length=254, unique=True)
    first_name = models.CharField(_('First Name'), max_length=120)
    last_name = models.CharField(_('Last Name'), max_length=120)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = SiteUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin

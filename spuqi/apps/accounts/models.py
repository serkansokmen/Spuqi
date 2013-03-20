from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _


class SiteUser(AbstractUser):
    avatar = models.ImageField(
        _('Avatar'),
        upload_to='avatars/%Y/%m/%d/',
        blank=True,
        null=True
    )

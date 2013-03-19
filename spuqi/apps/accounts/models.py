from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from django.conf import settings


class SiteUser(AbstractUser):
    avatar = models.ImageField(
        _('Avatar'),
        upload_to='%savatars' % settings.MEDIA_URL,
        blank=True,
        null=True
    )

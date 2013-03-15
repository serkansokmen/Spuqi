from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _


class SiteUser(AbstractUser):
    mugshot = models.ImageField(
        _('Cluster logo'),
        upload_to='mugshots',
        blank=True,
        null=True
    )

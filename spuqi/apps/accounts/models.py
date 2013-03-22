from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from easy_thumbnails.fields import ThumbnailerImageField


class SiteUser(AbstractUser):

    avatar = ThumbnailerImageField(
        verbose_name=_('Avatar'),
        upload_to='avatars/%Y/%m/%d/',
        resize_source={'size': (120, 120)},
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.get_full_name() if self.get_full_name() else self.username

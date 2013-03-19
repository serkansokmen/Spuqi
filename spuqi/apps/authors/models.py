from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from libs.utils import slugify
from apps.helpers.models import TimeStampedModel


class Author(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(_('Name'), max_length=255, unique=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['name', '-created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})

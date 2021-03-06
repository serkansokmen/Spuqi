from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from apps.authors.models import Author
from apps.helpers.models import TimeStampedModel
from libs.utils import slugify


class Source(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(_('Title'), max_length=250, unique=True)
    slug = models.SlugField()
    authors = models.ManyToManyField(Author, verbose_name=_('Authors'))
    web_address = models.URLField(_('Web Address'), blank=True)
    isbn = models.CharField(_('ISBN'), max_length=13, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Source, self).save(*args, **kwargs)

    def delete(self):
        super(Source, self).delete()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('source_detail', kwargs={'slug': self.slug})

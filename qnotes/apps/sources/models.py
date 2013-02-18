from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from qnotes.apps.authors.models import Author
from libs.utils import slugify
from django.utils.translation import ugettext as _


class Source(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(_('Title'), max_length=250, unique=True)
    slug = models.SlugField(max_length=250, editable=False, blank=True, null=True)
    authors = models.ManyToManyField(Author, verbose_name=_('Authors'))
    url = models.URLField(_('URL'), blank=True, null=True)
    isbn = models.CharField(_('ISBN'), max_length=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Source, self).save(*args, **kwargs)

    def delete(self):
        super(Source, self).delete()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('source_detail', kwargs={'slug': self.slug})

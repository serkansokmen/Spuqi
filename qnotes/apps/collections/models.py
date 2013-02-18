from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from qnotes.apps.sources.models import Source
from libs.utils import slugify
from django.utils.translation import ugettext as _


class Collection(models.Model):
    user = models.ForeignKey(User, related_name='owned_collections')
    title = models.CharField(_('Title'), max_length=100)
    slug = models.SlugField(max_length=100, editable=False, blank=True, null=True)
    sources = models.ManyToManyField(Source, verbose_name=_('Sources'),
            blank=True, null=True)
    members = models.ManyToManyField(User, related_name='followed_collections',
                                verbose_name=_('Members'), blank=True, null=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Collection, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('collection_detail', kwargs={'slug': self.slug})

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from qnotes.apps.sources.models import Source
from qnotes.apps.topics.models import Topic
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager


class Quote(models.Model):

    NOTE_TYPES = ((1, _('Text')), (2, _('Voice')), (3, _('Video')))

    user = models.ForeignKey(User)
    source = models.ForeignKey(Source, default=0, verbose_name=_('Source'))
    quote = models.TextField(_('Quote'), max_length=1200)
    note_type = models.PositiveIntegerField(_('Note type'), choices=NOTE_TYPES, blank=True, null=True)
    note = models.TextField(_('Note'), blank=True, max_length=500)
    topics = models.ManyToManyField(Topic, blank=True, verbose_name=_('Topics'))
    tags = TaggableManager(blank=True)
    is_private = models.BooleanField(_('Is private'), default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('quote_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Quote, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

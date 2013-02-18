from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from qnotes.apps.sources.models import Source
from qnotes.apps.topics.models import Topic
from django.utils.translation import ugettext as _


class Quote(models.Model):
    user = models.ForeignKey(User)
    source = models.ForeignKey(Source, default=0, verbose_name=_('Source'))
    quote = models.TextField(_('Quote'), blank=True, null=True, max_length=1200)
    note = models.TextField(_('Note'), blank=True, null=True, max_length=500)
    topics = models.ManyToManyField(Topic, blank=True, verbose_name=_('Topics'))
    is_private = models.BooleanField(_('Is private'), default=False)

    def __unicode__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('quote_detail', kwargs={'pk': self.pk})

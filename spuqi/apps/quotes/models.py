from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.dispatch import receiver
from apps.sources.models import Source
from apps.helpers.models import TimeStampedModel
from taggit.managers import TaggableManager
from libs.utils import slugify
import secretballot


class Note(TimeStampedModel):

    MEDIA_TYPES = (
        (1, _('Text')),
        (2, _('Voice')),
        (3, _('Video')))

    quote = models.ForeignKey('Quote')
    media_type = models.PositiveIntegerField(
        _('Note type'), choices=MEDIA_TYPES, default=1)
    text_note = models.TextField(_('Text'), blank=True)
    video_url = models.URLField(_('Video URL'), blank=True)
    sound_url = models.URLField(_('Sound URL'), blank=True)

    order = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        if self.media_type == 1:
            return self.text_note
        elif self.media_type == 2:
            return self.video_url
        elif self.media_type == 3:
            return self.sound_url

    class Meta:
        ordering = ['-order']


class Quote(TimeStampedModel):

    PRIVACY_STATES = (
        (1, _('Open to discussion')),
        (2, _('Read only')),
        (3, _('Private')),)
    OPEN = PRIVACY_STATES[0][0]
    READ_ONLY = PRIVACY_STATES[1][0]
    PRIVATE = PRIVACY_STATES[2][0]

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    source = models.ForeignKey(
        Source, verbose_name=_('Source'))
    quote = models.TextField(_('Quote'), max_length=1200)
    slug = models.SlugField()
    tags = TaggableManager(blank=True)
    privacy_state = models.PositiveSmallIntegerField(
        _('Privacy state'), choices=PRIVACY_STATES, default=2)

    def __unicode__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('quote_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = '%s-%s' % (
            slugify(self.source.title), slugify(self.quote))
        super(Quote, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']


secretballot.enable_voting_on(Quote)


@receiver(pre_save, sender=Quote)
def truncater(sender, instance, **kwargs):
    if sender is Quote:
        if len(instance.slug) > 50:
            instance.slug = instance.slug[:50]
